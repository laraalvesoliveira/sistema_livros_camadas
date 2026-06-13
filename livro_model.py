class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor
        }