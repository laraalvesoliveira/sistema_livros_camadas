import requests

class LivroRepository:
    def __init__(self):
        self.url = "http://127.0.0.1:5000/livros"

    def listar(self):
        resposta = requests.get(self.url)
        return resposta.json()

    def cadastrar(self, livro):
        requests.post(self.url, json=livro.to_dict())