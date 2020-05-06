# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
Central Estrutural -
Sara - Sistema de Análise de Dados com Redes Complexas e Analytics
Focado em análises politicas no twitter.
Realiza o calculo de centralidade
"""
import networkx as nx

import core.centralidade as relevante


class Importancia():
    """docstring for Estrutural."""

    def __init__(self, base, colecao, rede, nos=''):
        self.nome_base = base
        self.nome_colecao = colecao
        self.nome_rede = rede
        self.lista_nos = nos
        
    def carrega_grafo(self):
        """carrega um grafo e gera uma lista de vértices"""
        rede = nx.read_gml(self.nome_rede)
        self.lista_nos = rede.nodes()

    def realiza_busca(self):
        """realiza pesquisa na rede."""
        # self.lista_nos=["biakicis","mblivre","SenadorKajuru",
        # "joaoamoedonovo","QuebrandoOTabu","BolsonaroSP",
        # "CarlosBolsonaro",
        # "jose_neumanne","davialcolumbre"]
        # self.lista_nos=['mblivre',"biakicis","jose_neumanne"]
        nome_rede = self.nome_rede.split(".")[0]
        relevante.main(self.nome_base, self.nome_colecao,
                       self.lista_nos, nome_rede)

