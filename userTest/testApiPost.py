from requests import post, get, delete

# Пустой запрос
print(post('http://localhost:8080/api/v2/users').json())
# Неполный запрос
print(post('http://localhost:8080/api/v2/users',
           json={'name': 'Имя'}).json())
# Запрос с существующим id
print(post('http://localhost:8080/api/v2/users',
           json={'id': 1,
                 'surname': '',
                 'name': '',
                 'age': 35,
                 'position': "",
                 'speciality': '',
                 'address': "",
                 'email': ''}).json())

id = 638
# Правильный запрос
print(post('http://localhost:8080/api/v2/users',
           json={'id': id,
                 'surname': '',
                 'name': '',
                 'age': 35,
                 'position': "",
                 'speciality': '',
                 'address': "",
                 'email': ''}).json())

print(get(f'http://localhost:8080/api/v2/users/{id}').json())

print(delete(f'http://localhost:8080/api/v2/users/{id}').json())