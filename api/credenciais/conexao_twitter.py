# -*- coding: utf-8 -*-
"""
Inicia uma conexão com o twitter..
Remova as credencias ao realizar um upload para o git.
"""
import twitter


def inicia_conexao():
    """Abre a conexão com a api do twitter"""
    api = twitter.Api(
        consumer_key='1waQQ57sgxocirWyKT6i76CAy',
        consumer_secret='jc3F7Hz3Nw8PTiRqNHghkW00qmawcKsdmDt9cTrMu00NxRlCuK',
        access_token_key='1254887720528285697-JKIDq1ZCLFYU050HTaAl6mE1z9RKqU',
        access_token_secret='HwN8tPF1EqTiuSfPloMsiwG0MNJHrTEX8xiVRbeZcefse',
        sleep_on_rate_limit=True,
        tweet_mode='extended',
    )
    return api
