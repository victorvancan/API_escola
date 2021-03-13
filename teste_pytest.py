import requests

class TestCurso:
    headers = {'authorization': 'Token 5b708cdb6e0ba2dbbd4d183e4f5c0b84352e8345'}
    url_base_curso = 'http://localhost:8000/api/v2/cursos/'

    def test_get_curso(self):
        resposta = requests.get(url=self.url_base_curso, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_base_curso}5/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso de programação com Ruby",
            "url": "http://www.geekuniversity.com.br/cpr"
        }
        resposta = requests.post(url=self.url_base_curso, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo['titulo']
    def test_put_curso(self):
        atualizar = {
            "titulo" : "novo curso de ruby",
            "url": "http://www.geekuniversity.com.br/ncr"
        }

        resposta = requests.put(url=f'{self.url_base_curso}7/', headers=self.headers, data=atualizar)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "novo curso de ruby 2",
            "url": "http://www.geekuniversity.com.br/ncr2"
        }

        resposta = requests.put(url=f'{self.url_base_curso}7/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso(self):
        resposta = requests.delete(url=f'{self.url_base_curso}7/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0