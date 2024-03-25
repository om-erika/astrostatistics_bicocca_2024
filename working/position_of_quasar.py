# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:44:48 2024

@author: hp
"""

import numpy as np
from astroML.datasets import fetch_dr7_quasar
from matplotlib import pyplot as plt
import scipy.stats
import scipy.interpolate as interpolate
from scipy.interpolate import splev, splrep
import astropy
from scipy.stats import norm

mean = 1
sigma = 0.2
N = 5
gaussian = scipy.stats.norm(loc = mean, scale = sigma)
ax = plt.gca()
x = scipy.stats.norm.rvs(loc = mean, scale = sigma, size = N)
x.sort()
x_lin = np.linspace(0,2,500)
ax.plot(x_lin, gaussian.pdf(x_lin))
plt.title('Underlying process distribution')
plt.xlabel('x')
plt.ylabel('pdf(x)')
plt.show()

tot_likelihood = 1

#choose if homodastic or heterodastic errors 
sigma_x = np.full(N, sigma)
#sigma_x = np.abs(scipy.stats.norm.rvs(loc = 0.2, scale = 0.5, size = N))

for value, sigma_value in zip(x,sigma_x):
    ax = plt.gca()
    gauss = scipy.stats.norm(loc = value, scale = sigma_value)
    ax.plot(x_lin, gauss.pdf(x_lin), label = 'Likelihood for %.02f' %value)
    tot_likelihood = tot_likelihood*gauss.pdf(x_lin)

plt.legend()
plt.title('Plot of single likelihoods')
plt.xlabel('x')
plt.ylabel(r'$\mathcal{L}$(x)')
plt.show()
ax = plt.gca()    
ax.plot(x_lin, tot_likelihood)
plt.title('Plot of likelihoods product')
plt.xlabel('x')
plt.ylabel(r'$\Pi$ $\mathcal{L}$(x)')
plt.show()

ax = plt.gca()
tot_likelihood = np.log(tot_likelihood)
ax.plot(x_lin, tot_likelihood)   
findmax = x_lin[np.argmax(tot_likelihood)]
ax.axvline(findmax, label = r'max($\ln{\Pi\mathcal{L}(x)}$ = %.02f' % findmax, color = 'orange')
ax.axvline(mean, label = 'real mean = %.02f' % mean, color = 'green')
plt.title('Maximum Likelihood')
plt.xlabel('x')
plt.ylabel(r'$\ln{\Pi\mathcal{L}(x)}$')
plt.legend()
plt.show()

MLE_mean = sum(x/sigma_x**2)/sum(1/sigma_x**2)
print('Comparison between max of the likelihood and MLE estimator: %.02f, %.02f' % (findmax, MLE_mean))

fisher = 1/np.sqrt(- np.diff(tot_likelihood,n=2)[np.argmax(tot_likelihood)]/(x_lin[1]-x_lin[0])**2)
MLE_fisher = sum(1/sigma_x**2)**(-1/2)
print('Comparison between fisher matrix and MLE estimator: %.02f, %.02f' %(fisher, MLE_fisher))