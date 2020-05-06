# -*- coding: utf-8 -*-
from flask import Flask, request

from controllers.sara_centralidade import Importancia

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
    finally:
        return response