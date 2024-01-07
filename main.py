from flask import Flask, render_template, request, redirect, url_for
import random

from Jogo import Jogo
from Level import Level

app = Flask(__name__)

jogo = Jogo()
level = Level()


@app.route('/')
def index():
    return render_template('menu.html')


@app.route('/iniciar')
def iniciar():
    return render_template('cadastro-palavra.html', numero_palavras_cadastradas=len(jogo.palavras))


# Cadastro de palavras
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    palavra = request.form['palavra'].lower()
    jogo.addPalavra(palavra)
    if len(jogo.palavras) == jogo.numeroPalavras:
        level.palavras= jogo.palavras
        return redirect(url_for('jogar'))
    return redirect(url_for('iniciar'))

# Fases de Jogo
@app.route('/jogar')
def jogar():
    if jogo.estado == 0:
        jogo.estado=1
    if jogo.estado == 1 and level.vez==2:
        jogo.level=2
        
    return render_template('jogo.html', pontos_time_a=jogo.ponto1,pontos_time_b=jogo.ponto2,time_da_vez=timeDaVez())

def timeDaVez():
    if level.vez ==1:
        return "Jogada do time A"
    if level.vez ==2:
        return "Jogada do time B"
    return "ERRO"


@app.route('/começar-level')
def comecarLevel():
    level.trocaVez()
    jogo.checkLevel(level.vez)
    return render_template('valendo.html', palavra1 = level.buscaPalavra(), time=60)


@app.route('/enviar-time', methods=['POST'])
def enviarTime():
    level.addPalavra(level.escolhida)
    return render_template('valendo.html', palavra1 = level.buscaPalavra())


if __name__ == '__main__':
    app.run(debug=True)
