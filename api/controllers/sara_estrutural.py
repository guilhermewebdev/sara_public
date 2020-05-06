# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
Central Estrutural -
Sara - Sistema de Análise de Dados com Redes Complexas e Analytics
Focado em análises politicas no twitter.
Geração da rede
"""
# system import
import sys

# intern import
import core.rede_retweets as rede


def main(
    nome_rede,
    nome_base,
    nome_colecao,
    direcionada,
    limite,
):
    """Inicia a geração da rede."""
 
    rede.main(nome_rede, nome_base,
              nome_colecao, direcionada, limite)
