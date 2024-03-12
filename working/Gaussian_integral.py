# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:47:21 2024

@author: hp
"""

import numpy as np
from matplotlib import pyplot as plt
import scipy

#f(x) che rimane dopo aver separato p(x)
def function(x):
    return x**3

sigma = np.linspace(1, 1000)  #test per differenti valori di sigma
N = int(1e5)
# =============================================================================
# CASO 1: UTILIZZO UNA DISTRIBUZIONE GAUSSIANA DA -INFINITO A + INFINITO:
#   IN QUESTO CASO, DEVO AGGIUNGERE UN VALORE ASSOLUTO PER OTTENERE SOLO
#   VALORI POSITIVI PER X
# =============================================================================
# CASO 2: UTILIZZO UNA DISTRIBUZIONE HALF-GAUSSIANA DA 0 A + INFINITO:
#   IN QUESTO CASO, NON DEVO CORREGGERE I VALORI DI X PERCHÉ LA PDF É DEFINITA
#   SOLAMENTE NELL'INTERVALLO POSITIVO 0, +INFINITO
# =============================================================================
for s in sigma:
    gauss = scipy.stats.norm(loc = 0 , scale=s)
    draws = np.abs(gauss.rvs(N))
    
    plt.hist(draws)
    integral_1 = np.mean(function(draws))*np.sqrt(2*np.pi)*s/2
    
    gauss = scipy.stats.halfnorm(loc = 0 , scale=s)
    draws = gauss.rvs(N)
    
    plt.hist(draws)
    integral_2 = np.mean(function(draws))*np.sqrt(2*np.pi)*s/2
    
    print(integral_1/(2*s**4), integral_2/(2*s**4)) #verifica che rapporto sia = 1