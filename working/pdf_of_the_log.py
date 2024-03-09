# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:09:48 2024

@author: hp
"""

import numpy as np
from matplotlib import pyplot as plt

N = 500000

#pdf per distribuzione uniforme
x = np.random.rand(N)
plt.hist(x, bins = 100, density = True)
plt.title('PDF for uniform distribution')
plt.xlabel('x')
plt.ylabel('PDF(x)')
print(np.mean(np.log10(x)), np.median(np.log10(x)))
plt.show()

#pdf per y = log10(x), partendo da una distribuzione uniforme
y = np.log10(x)
print(np.mean(y), np.median(y))
plt.hist(y, bins = 100, density = True)
plt.xlabel('y')
plt.ylabel('PDF(y)')
plt.title(r'PDF for y = $log_{10}(x)$, where x has a uniform distribution')

#calcolo pdf teorica, tramite inverso della derivata
y_py = np.linspace(min(y), max(y), N)
p_y = np.abs(10**y_py*np.log(10))
plt.plot(y_py, p_y)
plt.vlines(max(y), 0, max(p_y), color = 'orange')
plt.show()

#pdf per y = e^x, partendo da una distribuzione uniforme
print(np.mean(np.exp(x)), np.median(np.exp(x)))
y = np.exp(x)
print(np.mean(y), np.median(y))
plt.hist(y, bins = 100, density = True)
plt.title(r'PDF for y = $e^{x}$, where x has a uniform distribution')
plt.xlabel('y')
plt.ylabel('PDF(y)')

#calcolo pdf teorica, tramite inverso della derivata
y_py = np.linspace(min(y), max(y), N)
p_y = np.abs(1/y_py)
plt.plot(y_py, p_y)
plt.vlines(min(y), 0, max(p_y), color = 'orange')
plt.vlines(max(y), 0, min(p_y), color = 'orange')

