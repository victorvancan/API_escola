import requests

headers = {'authorization': 'Token 5b708cdb6e0ba2dbbd4d183e4f5c0b84352e8345'}

url_base_curso = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Gerência agil de projetos com Scrum",
    "url": "http://www.geekuniversity.com.br/scrum"
}

resultado = requests.post(url=url_base_curso, headers=headers, data=novo_curso)

# TEstando o codgo de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
