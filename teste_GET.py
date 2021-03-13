import requests

headers = {'authorization': 'Token 5b708cdb6e0ba2dbbd4d183e4f5c0b84352e8345'}

url_base_curso = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_curso, headers=headers)

print(resultado.json())

# Testando se o endpoint esta correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 5

# Testando se o título do primerio curso está correto
assert  resultado.json()['results'][0]['titulo'] == 'Algoritmos e Lógica de Programação do básico ao avançado'