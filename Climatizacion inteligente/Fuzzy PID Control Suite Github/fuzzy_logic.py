#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 11:00:04 2024

@author: antiXLinux
"""

import numpy as np 
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Definiendo las variables de entrada y salida 

temperatura = ctrl.Antecedent(np.arange(0, 51, 1), 'temperatura')
calor = ctrl.Consequent(np.arange(0, 101, 1), 'calor')


def fuzzy():
    
    """
    .
    Función que establece los conjuntos, reglas y sistema difuso 
    """
    
    # crear los conjuntos difusos # trimf es para funciones de membresia personalizadas

    temperatura['frio']= fuzz.trimf(temperatura.universe, [0, 0, 20]) 
    temperatura['comodo']= fuzz.trimf(temperatura.universe, [10, 20, 30]) 
    temperatura ['caliente']= fuzz.trimf(temperatura.universe, [20, 50, 50]) 

    calor['bajo']= fuzz.trimf(calor.universe, [0, 0, 50])
    calor['medio']= fuzz.trimf(calor.universe, [0, 50, 100])
    calor['alto']= fuzz.trimf(calor.universe, [50, 100, 100])
    
    # definir las reglas difusas 

    regla1 = ctrl.Rule(temperatura['frio'], calor['alto'])
    regla2 = ctrl.Rule(temperatura['comodo'], calor['medio'])
    regla3 = ctrl.Rule(temperatura['caliente'], calor['bajo'])
    
    # crear sistema de control difuso

    sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
    sistemaf = ctrl.ControlSystemSimulation(sistema_control)
    
    return sistemaf   # necesario que devuelva el sistema para adquirir los atributos 


def evaluar_temperatura(sistemaf, temp):
    
    """
    .
    Función que evalua la temperatura de entrada en un instante t 
    """
    
    sistemaf.input['temperatura'] = temp
    sistemaf.compute()
    valor_calor_fuzzy = sistemaf.output['calor']
    #print(valor_calor_fuzzy)
    #temperatura.view(sim=sistemaf) #Graficos de entrada y salida opcional para otros proyecto
    #calor.view(sim=sistemaf)
    
    return valor_calor_fuzzy


if __name__ == "__main__":
    
    sistemaf = fuzzy()
    evaluar_temperatura(sistemaf, 27)
    #evaluar_temperatura(sistemaf, 17)
    #evaluar_temperatura(sistemaf, 28)


    

    
    
    
    
    
    