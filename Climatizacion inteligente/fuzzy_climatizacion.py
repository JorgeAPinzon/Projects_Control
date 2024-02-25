#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 16:52:06 2024

@author: antiXLinux
"""

import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definiendo las variables de entrada y salida 

temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
calor = ctrl.Consequent(np.arange(0, 101, 1), 'calor')

# crear los conjuntos difusos # trimf es para funciones de membresia personalizadas

temperatura['frio']= fuzz.trimf(temperatura.universe, [0, 0, 20]) 
temperatura['comodo']= fuzz.trimf(temperatura.universe, [10, 20, 30]) 
temperatura ['caliente']= fuzz.trimf(temperatura.universe, [20, 50, 50]) 

calor['bajo']= fuzz.trimf(calor.universe, [0, 0, 50])
calor['medio']= fuzz.trimf(calor.universe, [0, 50, 100])
calor['alto']= fuzz.trimf(calor.universe, [50, 100, 100])

# ahora puede ver como se ven con .view()
#calor.view()
#temperatura.view()

# definir las reglas difusas 

regla1 = ctrl.Rule(temperatura['frio'], calor['alto'])
regla2 = ctrl.Rule(temperatura['comodo'], calor['medio'])
regla3 = ctrl.Rule(temperatura['caliente'], calor['bajo'])

# crear sistema de control difuso

sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# simular el sistema de control difuso 

sistema.input['temperatura'] = 26
sistema.compute()
print(sistema.output['calor'])
calor.view(sim = sistema)


