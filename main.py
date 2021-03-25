from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import Flask, url_for, request, render_template, redirect
import datetime
from flask_login import LoginManager, login_manager, login_required, login_user, logout_user
from forms.user import LoginForm, RegisterForm

db_session.global_init("db/blogs.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
@app.route('/index')
def index():
    jobs = []
    session = db_session.create_session()
    for i in session.query(Jobs).all():
        jobs.append((i.job,
                     i.leader.name,
                     i.leader.surname,
                     i.work_size,
                     i.collaborators,
                     i.if_finished))
    session.close()
    params = {}
    print(jobs)
    params["title"] = "Журнал работ"
    params["static_css"] = url_for('static', filename="css/")
    params["static_img"] = url_for('static', filename="img/")
    params["jobs"] = jobs
    return render_template('index.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    params = {}
    params["title"] = "Авторизация"
    params["static_css"] = url_for('static', filename="css/")
    params["static_img"] = url_for('static', filename="img/")

    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form, **params)
    return render_template('login.html', form=form, **params)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    params = {}
    params["title"] = "Регистрация"
    params["static_css"] = url_for('static', filename="css/")
    params["static_img"] = url_for('static', filename="img/")

    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', **params, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=8080, host='127.0.0.1')
