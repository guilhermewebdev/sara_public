# -*- coding: utf-8 -*-
from flask import Flask, request

from controllers.sara_centralidade import Importancia
from controllers.sara_coletor import coletar

app = Flask(__name__)


@app.route('/centralidade',  methods=['POST'])
def centralidade():
    response = {}
    try:
        importancia = Importancia(
            base=request.form['base'],
            colecao=request.form['colecao'],
            rede=request.form['rede'],
        )
        importancia.carrega_grafo()
        importancia.realiza_busca()
        response['sucess'] = True
    except KeyError as err:
        response['error'] = err
        response['sucess'] = False
    else:
        response['sucess'] = False
    finally:
        return response

@app.route('/coletor', methods=['POST'])
def coletor():
    response = {}
    try:
        coletar(
            name_file=request.form['arquivo'],
            termo=request.form['termo'],
            n_tweets=request.form['n_tweets'],
            colecao=request.form['colecao'],
            nome_banco=request.form['banco']
        )
    except KeyError as err:
        response['error'] = err
        response['sucesss'] = False
    else:
        response['sucess'] = False
    finally:
        return response