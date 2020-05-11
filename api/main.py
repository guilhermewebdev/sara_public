# -*- coding: utf-8 -*-
from flask import Flask, request

from controllers.sara_centralidade import Importancia
from controllers.sara_coletor import coletar
from controllers.sara_conteudo import modelar
from controllers.sara_estrutural import main
from controllers.sara_sentimento import DetectorSentimento

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
        response['success'] = True
    except KeyError as err:
        response['error'] = err
        response['success'] = False
    else:
        response['success'] = False
    finally:
        return response


@app.route('/coletor', methods=['POST'])
def coletor():
    response = {}
    try:
        response['success'] = True
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
        response['success'] = False
    finally:
        return response


@app.route('/conteudo', methods=['POST'])
def conteudo():
    try:
        modelar(
            name_file=request.form['arquivo'],
            banco=request.form['banco'],
            colecao=request.form['colecao']
        )
        response['success'] = True
    except KeyError as err:
        response['error'] = err
        response['sucesss'] = False
    else:
        response['success'] = False
    finally:
        return response


@app.route('/estrutural', methods=['POST'])
def estrutural():
    try:
        main(
            nome_rede=request.form['rede'],
            nome_base=request.form['base'],
            colecao=request.form['colecao'],
            direcionada=request.form['direcionada'],
            limite=request.form['limite'],
        )
        response['success'] = True
    except KeyError as err:
        response['error'] = err
        response['sucesss'] = False
    else:
        response['success'] = False
    finally:
        return response

@app.route('/sentimento', methods=['POST'])
def sentimento():
    try:
        detecta_sentimento = DetectorSentimento()
        detecta_sentimento.main(
            request.form['database_name'],
            request.form['collection']
        )
        response['success'] = True
    except KeyError as err:
        response['error'] = err
        response['sucesss'] = False
    else:
        response['success'] = False
    finally:
        return response