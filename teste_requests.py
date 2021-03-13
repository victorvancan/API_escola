import requests

# get avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# acessando o codigo de status http
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# acessano a quantidade de registros
# print(avaliacoes.json()['count'])

# acessando a proxima pagina
# print(avaliacoes.json()['next'])

# acessando os resultados desta pagina
# print(avaliacoes.json()['results'])
# print (type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# Acessando o ultimo elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

 # Acessando somente o nome da pessoa que fez a ultima avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GEt Avaliacao

headers = {'authorization': 'Token 5b708cdb6e0ba2dbbd4d183e4f5c0b84352e8345'}

avaliacao = requests.get(url='http://localhost:8000/api/v2/avaliacoes/3/', headers=headers)

print(avaliacao.json())
print(avaliacao.status_code)