#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 11:02:49 2024

@author: antiXLinux
"""

import numpy as np 
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt                     # para realizar el plot 3D degrado agradable
from mpl_toolkits.mplot3d import Axes3D             # Requerido para graficar en 3D 

# El universo disperso hace los calculos mas rapidos, sin sacrificar la precisión 
# Aqui solo se incluyen los puntos criticos; hacerlo de mayor resolucion es innecesario

universo = np.linspace(-2, 2, 5)

# Crear las 3 variables difusas, dos entradas una salida 

error = ctrl.Antecedent(universo, 'error')
delta = ctrl.Antecedent(universo, 'delta')
output = ctrl.Consequent(universo, 'output')

#  Aqui usamos la conveniencia 'automf' para poblar las variables difusas con terminos.
# El kwarg opcional 'names=' nos permite especificar los nombre de nuestros terminos

names = ['nb', 'ns', 'ze', 'ps', 'pb']
error.automf(names = names)
delta.automf(names = names)
output.automf(names = names)

# definicion del conjunto de reglas complejas 

regla0 = ctrl.Rule(antecedent = ((error['nb'] & delta['nb']) |
        (error['ns'] & delta['nb']) |
        (error['nb'] & delta['ns'] )), consequent = output['nb'], label = 'rule nb')

regla1 = ctrl.Rule(antecedent = ((error['nb'] & delta['ze']) |
        (error['nb'] & delta['ps']) |
        (error['ns'] & delta['ns']) |
        (error['ns'] & delta['ze']) |
        (error['ze'] & delta['ns']) |
        (error['ze'] & delta['nb']) |
        (error['ps'] & delta['nb'] )), consequent = output['ns'], label = 'rule ns')

regla2 = ctrl.Rule(antecedent = ((error['nb'] & delta['pb']) |
        (error['ns'] & delta['ps']) |
        (error['ze'] & delta['ze']) |
        (error['ps'] & delta['ns']) |
        (error['pb'] & delta['nb'] )), consequent = output['ze'], label = 'rule ze')

regla3 = ctrl.Rule(antecedent = ((error['ns'] & delta['pb']) |
        (error['ze'] & delta['pb']) |
        (error['ze'] & delta['ps']) |
        (error['ps'] & delta['ps']) |
        (error['ps'] & delta['ze']) |
        (error['pb'] & delta['ze']) |
        (error['pb'] & delta['ns'] )), consequent = output['ps'], label = 'rule ps')

regla4 = ctrl.Rule(antecedent = ((error['ps'] & delta['pb']) |
        (error['pb'] & delta['pb']) |
        (error['pb'] & delta['ps'] )), consequent = output['pb'], label = 'rule pb')

# A continuacion añadimos estas reglas a un nuevo ControlSystem y definimos un ControlSystemSimulation para ejecutarlo.

sistema = ctrl.ControlSystem(rules = [regla0, regla1, regla2, regla3, regla4])

#Mas tarde tenemos la intencion de ejecutar este sistema con un conjunto de 21 X 21 entradas, 
#por lo que permitimos muchas mas que una unica ejecucion, antes de que los resultados se vacien. 
#Las ejecuciones posteriores volverian un 1/8 del tiempo

sim = ctrl.ControlSystemSimulation(sistema, flush_after_run = 21 * 21 + 1)

# Con el util uso de Matplotlib y simulaciones repetidas, 
# podemos observar el aspecto de toda la superficie del sistema de control en tres dimensiones
# podemos simular a mayor resolucion con total precision

upsampled = np.linspace(-2, 2, 21)
x, y = np.meshgrid(upsampled, upsampled) # matrices de coordenadas 
# z = np.zeros_like                        # matrices cuyos componentes son ceros 
z = np.zeros((21, 21))                      # Inicializa z como una matriz de ceros de tamaño 21x21

# Recorre el sistema 21 X 21 veces para recoger la superficie de control 
for i in range(21):
    for j in range(21):
        sim.input['error'] = x[i, j]
        sim.input['delta'] = y[i, j]
        sim.compute()
        output_value = sim.output['output']  # Almacena el valor de output en una variable
        z[i, j] = output_value  # Asigna el valor almacenado en z[i, j]
        
# realizando el plot con las librerias listadas 
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride = 1, cstride = 1, cmap = 'viridis', linewidth = 0.4, antialiased = True)

cset = ax.contourf(x, y, z, zdir = 'z', offset = -2.5, cmap = 'viridis', alpha = 0.5) # sombreado bajo la grafica que proyecta lo
cset = ax.contourf(x, y, z, zdir = 'x', offset = 3, cmap = 'viridis', alpha = 0.5) # que pasa en los dos ejes 
cset = ax.contourf(x, y, z, zdir = 'y', offset = 3, cmap = 'viridis', alpha = 0.5)

ax.view_init(30, 200) #Un valor de 30 significa que la cámara está elevada a 30 grados por encima del plano horizontal1.
                      #Un valor de 200 significa que la cámara ha girado 200 grados en sentido antihorario desde el eje x1.
























