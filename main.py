from flask import Flask

app = Flask(__name__)


# Rota principal
@app.route("/")
def home():
    return "Bem-vindo à página inicial!"


# Rota sobre
@app.route("/sobre")
def sobre():
    return "Essa é a página sobre o projeto."


# Rota como parâmetro
@app.route("/usuario/<username>")
def usuario(username):
    return f"Bem-vindo(a) {username}!"


if __name__ == "__main__":
    app.run(debug=True)
