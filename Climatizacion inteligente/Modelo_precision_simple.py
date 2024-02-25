#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 14:52:23 2024

@author: antiXLinux
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Recopilar datos

temperaturas = np.array([26, 27, 28, 29, 30, 31]).reshape((-1, 1)) # matriz de una sola columna
calor_frio = np.array([40, 35, 30, 25, 20, 20])

# Preprocesar los datos 

temperaturas = temperaturas / 100.0
calor_frio = calor_frio / 100.0

# Crear y entrenar el modelo

modelo = LinearRegression()
modelo.fit(temperaturas, calor_frio)

# Evaluar el modelo           ojo que hasta aca va el predictor

print(modelo.predict(np.array([[0.28]]))) #En este caso, se está prediciendo un valor utilizando el modelo (modelo.predict()) 
                                           #y pasando un único valor (0.26) como entrada 26 grados

# LO QUE HAY DE ACA PARA ABAJO SOLO ES UNA COMPARACION DE PREDICCION VS ENFOQUE FUZZY USANDO SOLO EL MSE error cuadratico medio
                                           
                                           
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


# Supongamos que tus datos de prueba son:
temperaturas_prueba = np.array([26, 27, 28, 29, 30, 31]) / 100.0
calor_frio_real = np.array([40, 35, 30, 25, 20, 20]) / 100.0

# Aplicar el control difuso a los datos de prueba
calor_frio_difuso = []


for temp in temperaturas_prueba:
    sistema.input['temperatura'] = temp * 100
    sistema.compute()
    calor_frio_difuso.append(sistema.output['calor'] / 100)

# Aplicar el modelo predictivo a los datos de prueba

calor_frio_predicho = modelo.predict(temperaturas_prueba.reshape((-1, 1)))

# Calcular el error cuadrático medio para cada método
error_difuso = np.mean((calor_frio_real - calor_frio_difuso) ** 2)
error_prediccion = np.mean((calor_frio_real - calor_frio_predicho) ** 2)

print('error cuadratico MSE difuso',error_difuso)
print('error cuadratico MSE prediccion', error_prediccion)

# print(sistema.output['calor']) # para este caso es la ultimo valor calculado y registrado en el arreglo calor_frio_difuso
#calor.view(sim = sistema) # para este caso es la ultimo valor calculado y registrado en el arreglo calor_frio_difuso





















