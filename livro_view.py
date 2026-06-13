from livro_service import LivroService

class LivroView:
    def __init__(self):
        self.service = LivroService()

    def menu(self):
        while True:
            print("\n=== Sistema de Livros ===")
            print("1 - Listar livros")
            print("2 - Cadastrar livro")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar()
            elif opcao == "2":
                self.cadastrar()
            elif opcao == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

    def listar(self):
        livros = self.service.listar_livros()

        print("\nLivros cadastrados:")
        for livro in livros:
            print("Título:", livro["titulo"], "- Autor:", livro["autor"])

    def cadastrar(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")

        self.service.cadastrar_livro(titulo, autor)