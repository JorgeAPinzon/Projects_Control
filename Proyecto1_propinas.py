#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:29:36 2024

@author: antiXLinux
"""

import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# definicion de las variables difusas 

# nuevos objetos antecedentes/ consecuentes variables hold y funciones de membresia 

calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# la poblacion de la funcion de auto-membresia es posible con .automf(3,5,7)

calidad.automf(3)
servicio.automf(3)

# Las funciones de membresia personalizadas se pueden crear de forma interactiva con una API Python familar

propina['low'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['medium'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['high'] = fuzz.trimf(propina.universe, [13, 25, 25])

# ahora puede ver como se ven con .view()
#calidad['average'].view()
#servicio.view()
#propina.view()


# grafico de las reglas que se consideran aceptadas por la "mayoria"
#If la comida es pobre OR el servicio es pobre, then la propina sera baja 
#If el servicio es promedio, then la propina sera media 
#If la comida es buena OR el servicio es bueno, then la propina sera alta

regla1 = ctrl.Rule(calidad['poor'] | servicio['poor'], propina['low'])
regla2 = ctrl.Rule(servicio['average'], propina['medium'])
regla3 = ctrl.Rule(servicio['good'] | calidad['good'], propina['high'])

#regla3.view()

propina_ctrl = ctrl.ControlSystem([regla1, regla2, regla3]) #sistema de control 
propin_a = ctrl.ControlSystemSimulation(propina_ctrl)       #simulacion 


# NOTA: Si le gusta pasar muchas entradas a la vez, use .Inputs (dict_of_data)
# Supongamos que tienes más entradas como 'ambience' y 'price'
#input_data = {'quality': 6.5, 'service': 9.8, 'ambience': 7.5, 'price': 8.0}
# Pasas todas las entradas al sistema de control difuso a la vez
#tipping.inputs(input_data)
# Pase las entradas al sistema de control utilizando etiquetas antecedentes con API python

propin_a.input['calidad'] = 6.5
propin_a.input['servicio'] = 9.8




#poner y computar  los numeros 
propin_a.compute()

print propin_a.output['propina']
propina.view(sim=propin_a)





