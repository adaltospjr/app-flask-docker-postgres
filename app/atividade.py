from flask import Flask, render_template, request

import conexao

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("escopo.html")


@app.route("/gravar", methods=["POST"])
def gravar():
    nome = request.form["nome"]
    categoria = request.form["categoria"]
    preco = request.form["preco"]

    conexao.gravar(nome, categoria, preco)

    dados = conexao.consulta()

    return 'Os dados digitados foram salvos'


@app.route("/consultar")
def consultar():
    dados = conexao.consulta()
    return dados.to_html()


app.run(host="0.0.0.0", debug=True)
