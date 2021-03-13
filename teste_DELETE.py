import requests

headers = {'authorization': 'Token 5b708cdb6e0ba2dbbd4d183e4f5c0b84352e8345'}
url_base_curso = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

reusltado = requests.delete(url=f'{url_base_curso}7/', headers=headers)

# Testando o código HTTP
assert reusltado.status_code == 204

# Testando se o tamanho do conteúdo retorno é 0
assert len(reusltado.text) == 0