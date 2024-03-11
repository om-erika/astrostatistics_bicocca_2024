# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:29:19 2024

@author: hp
"""
import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt
from scipy import integrate
from scipy.stats import poisson

dati = pd.DataFrame(np.array(([0, 109], [1,65], [2,22], [3,3], [4,1])), index = None, columns = ['number of deaths', 'number of groups'])

dati['frequency'] = dati['number of groups']/200

plt.scatter(dati['number of deaths'], dati['frequency'])

mean = np.mean(dati['number of deaths'])
standard_dev = np.std(dati['number of deaths'])
median = np.median(dati['number of deaths'])
skewness = stats.skew(dati['number of deaths'])
kurtois = stats.kurtosis(dati['number of deaths'])
# =============================================================================
# mean = 2, median = 2, standard_dev = sqrt(2) in agreement 
# with the hypotesis of the frequency of deaths being poissonian 
# skewness and kurtois instead not very useful (i think)
# =============================================================================

dist = poisson(mean)
plt.plot(dati['number of deaths'], dist.pmf(dati['number of deaths']), label = r'$\mu$ = %0.2f' % mean)

#i try fitting by hand (?) with different values of the mean
means = np.linspace(0.1, 5, 11)
for mu in means:
    #only because 2.06 is close to the mean I get from the datas
    #but i want to still use linspace to have different values
    if mu != 2.06:
        dist = poisson(mu)
        plt.plot(dati['number of deaths'], dist.pmf(dati['number of deaths']), label = r'$\mu$ = %0.2f' % mu)

plt.legend(ncol = 2)
plt.title('Different poissonian fits for the datas')
plt.show()

# =============================================================================
# Is it right that 0.59 is a better mu than the value i get from the mean? 
# =============================================================================