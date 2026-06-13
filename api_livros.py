from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry"}
]

@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros)

@app.route("/livros", methods=["POST"])
def cadastrar_livro():
    novo_livro = request.json
    livros.append(novo_livro)
    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201

if __name__ == "__main__":
    app.run(debug=True)