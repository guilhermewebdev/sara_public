# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
Central de Análise de conteúdo do Framework Sara.
Gera a Núvem de palavras
"""
# import core.bagwords as bagwords
import sys

import core.modelagem_topicos as modelagem_topicos

def modelar(name_file, banco, colecao):
    # Análise de conteúdo
    palavras = modelagem_topicos.main(banco, colecao, 1000)
# print("Modelagem ... OK\nSentimento Modelagem:")
# print("Sentimento Modelagem... ok")
