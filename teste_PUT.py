import requests

headers = {'authorization': 'Token 5b708cdb6e0ba2dbbd4d183e4f5c0b84352e8345'}

url_base_curso = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo Curso de Scrum 2",
    "url": "http://www.geekuniversity.com.br/scrum2"
}

# Buscando o curso com ID 6=7
# curso = requests.get(url=f'{url_base_curso}7/', headers=headers)
#
# print(curso.json())

# resultado = requests.put(url=f'{url_base_curso}7/', headers=headers, data=curso_atualizado)
#
# # Testando o código de status HTTP
# assert resultado.status_code == 200
#
# # Testando o titulo
# assert resultado.json()['titulo'] == curso_atualizado['titulo']