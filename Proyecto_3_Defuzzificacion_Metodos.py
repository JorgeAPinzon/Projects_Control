#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 18:52:17 2024

@author: antiXLinux
"""

# proyecto No 3 defuzzificacion ademas del centroide de en algunas veces superposicion de los trapecios que se forman 

import numpy as np 
import matplotlib.pyplot as plt 
import skfuzzy as fuzz 

# generando una funcion de membresia trapezoidal en un rango de 0 a 1 

x = np.arange(0, 5.05, 0.1)
mfx = fuzz.trapmf(x, [2, 2.5, 3, 4.5])

# defuzzificando esta funcion de membresia de 5 maneras 

defuzz_centroide = fuzz.defuzz(x, mfx, 'centroid') # igual que skfuzzy.centroid
defuzz_bisector = fuzz.defuzz(x, mfx, 'bisector')
defuzz_mom = fuzz.defuzz(x, mfx, 'mom')
defuzz_som = fuzz.defuzz(x, mfx, 'som')
defuzz_lom = fuzz.defuzz(x, mfx, 'lom')

# recolectar informacion para lineas verticales
labels = ['centroide', 'bisector', 'media del maximo', 'minimo del maximo',
          'maximo del maximo']
xvals = [defuzz_centroide,
         defuzz_bisector,
         defuzz_mom,
         defuzz_som,
         defuzz_lom]
colors = ['r', 'b', 'g', 'c', 'm'] 
ymax = [fuzz.interp_membership(x, mfx, i) for i in xvals] # calculando los grados de membresia iterando valores y guardando en xvals

# Visualizacion y comparacion de los resultados de la defuzzificacion con la funcion de pertenencia
plt.figure(figsize=(8, 5))

plt.plot(x, mfx, 'k')

# hasta aca es la funcion de pertencia a continuacion en el ciclo for se evidencian los metodos 

for xv, y, label, color in zip(xvals, ymax, labels, colors):
    plt.vlines(xv, 0, y, label=label, color=color)
plt.ylabel('Funcion de pertenencia ')
plt.xlabel('Variable universo (arb)')
plt.ylim(-0.1, 1.1)
plt.legend(loc = 2)

plt.show()