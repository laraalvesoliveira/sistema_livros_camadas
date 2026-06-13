from livro_model import Livro
from livro_repository import LivroRepository

class LivroService:
    def __init__(self):
        self.repository = LivroRepository()

    def listar_livros(self):
        return self.repository.listar()

    def cadastrar_livro(self, titulo, autor):
        if titulo == "" or autor == "":
            print("Título e autor são obrigatórios.")
        else:
            livro = Livro(titulo, autor)
            self.repository.cadastrar(livro)
            print("Livro cadastrado com sucesso!")