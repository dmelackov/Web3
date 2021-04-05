from requests import post, get

# Пустой запрос
print(post('http://localhost:8080/api/jobs').json())
# Неполный запрос
print(post('http://localhost:8080/api/jobs',
           json={'title': 'Заголовок'}).json())
# Запрос с существующим id
print(post('http://localhost:8080/api/jobs',
           json={'id': 3,
                 'team_leader': 1,
                 'job': 'Сделать дз',
                 'work_size': 35,
                 'collaborators': "",
                 'if_finished': True}).json())

id = 634
# Правильный запрос
print(post('http://localhost:8080/api/jobs',
           json={'id': id,
                 'team_leader': 1,
                 'job': 'Сделать дз',
                 'work_size': 35,
                 'collaborators': "",
                 'if_finished': True}).json())

print(get(f'http://localhost:8080/api/jobs/{id}').json())
