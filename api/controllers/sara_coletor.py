# -*- coding: utf-8 -*-
"""
Framework de Análise de dados Politicos no twitter..
Central de Coleta Dados do Framework de Análise de Dados -
Sara - Sistema de Análise de Dados com Redes Complexas e Analytics
Focado em análises politicas no twitter.

Coletor API
"""
import sys

from core.sauron_coletor import Sauron
from core.logger import log
# padrao_pesquisa,limite,colecao,nome_banco="eleicao"
# coletor de dados


# termo="haddad"
# n_tweets=0
# colecao="haddad_2310"
# nome_banco="eleicao"

# termo colecao numero_tweets
def coletar(
    name_file,
    termo,
    n_tweets,
    colecao,
    nome_banco
):
    log(termo)
    coletor = Sauron()
    coletor.pesquisa(termo, n_tweets, colecao, nome_banco)

# odetalhista.detector_bots(nome_banco,colecao)
