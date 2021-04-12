from requests import get


print(get('http://localhost:8080/api/v2/users').json())
print(get('http://localhost:8080/api/v2/users/1').json())
print(get('http://localhost:8080/api/v2/users/0').json())
print(get('http://localhost:8080/api/v2/users/sdf'))