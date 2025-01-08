#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:59:04 2024

@author: antiXLinux
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Recopilar datos

temperatura2 = np.array([26, 27, 28, 29, 30,31]).reshape((-1, 1)) # matriz de una sola columna
calor2 = np.array([26, 27, 28, 20, 30, 31]) # datos iguales asumiendo un control ideal

# Modo testing ⬇⬇

#temperatura2 = np.array([18.18, 18.36, 18.54, 18.72, 18.9, 19.08, 19.26, 19.44, 19.62, 19.8, 19.98, 20.16, 20.34, 20.52, 20.7, 20.88, 21.06, 21.24, 21.42, 21.6, 21.78, 21.96, 22.14, 22.32, 22.5, 22.68, 22.86, 23.04, 23.22, 23.4, 23.58, 23.76, 23.94, 24.12, 24.3, 24.48, 24.66, 24.84, 25.02, 25.2, 25.38, 25.56, 25.74, 25.92, 26.1, 26.28, 26.46, 26.64, 26.82, 27]).reshape((-1, 1)) 
#temperatura2 = np.array([18, 18.36, 18.54, 18.72, 18.9, 19.08, 19.26, 19.44, 19.62, 19.8, 19.98, 20.16, 20.34, 20.2, 20, 20.08, 20.06, 19.84, 19.42, 19.6, 18.78, 18.96, 18.14, 17.32, 17.5, 16.68, 16.86, 17.04, 17.22, 17.4, 17.58, 17.76, 17.94, 18.12, 18.3, 18.48, 18.66, 18.84, 19.02, 19.2, 19.38, 18.56, 18.74, 17.92, 18.1, 18.28, 18.46, 18.64, 18.82, 19]).reshape((-1, 1))
#calor2 = np.array([18, 18, 18, 18, 19, 19, 19.46, 19.64, 19.82, 19.89, 20, 20, 20.3, 20.2, 20.1, 20.2, 20.16, 20.84, 20.42, 19.6, 18.28, 18.56, 18.44, 17.72, 17.5, 16.68, 16.86, 17.04, 17.22, 17.4, 17.58, 17.76, 17.94, 18.12, 18.3, 18.48, 18.66, 18.84, 19.02, 19.2, 19.38, 18.56, 18.74, 17.92, 18.1, 18.28, 18.46, 18.64, 18.82, 19])
#calor2 = np.array([18.1, 20, 21, 22, 21, 24, 22, 22.5, 22.7, 19.9, 20.1, 20.3, 21.5, 21.7, 19.9, 20.1, 21.3, 24.5, 22.7, 18.9, 19.1, 20.3, 24.5, 21.7, 22.9, 20.1, 15.3, 17.5, 18.7, 18.9, 22.1, 22.3, 20.5, 24.7, 24.9, 25.1, 26.3, 26.5, 27.7, 15.9, 16.1, 19.3, 18.5, 18.7, 18.9, 17.1, 20, 24.1, 27, 28])
#calor2 = np.array([20, 19.8, 20.2, 19.6, 20.4, 19.4, 20.6, 19.2, 20.8, 19, 21, 18.8, 21.2, 18.6, 21.4, 18.4, 21.6, 18.2, 21.8, 18, 22, 18.2, 22.2, 18.4, 22.4, 18.6, 22.6, 18.8, 22.8, 19, 23, 19.2, 23.2, 19.4, 23.4, 19.6, 23.6, 19.8, 23.8, 20, 24, 20.2, 24.2, 20.4, 24.4, 20.6, 24.6, 20.8, 24.8, 21])
#print(temperatura2)
#print(calor2)

def predict():
    """
    .
    Función que realiza un modelo de prediccion sencillo por medio de regresión lineal 

    Returns
    -------
    modelo : Regresión lineal conformada por temperatura2 y calor2.
    temperatura2 : Matriz de una sola columna que representa los datos de temperatura ingresados al sistema.
    calor2 : Datos de salida referidos a manera independiente(funcionamiento del sistema).

    """
    # preprocesar los datos al usar la palabra clave global, se puede modificar el valor de 
    # las variables 
    
    global temperatura2
    global calor2
    
    temperatura2 = temperatura2 / 100.0
    calor2 = calor2 / 100.0
    
    # Crear y entrenar el modelo

    modelo = LinearRegression()
    modelo.fit(temperatura2, calor2)
    
    return modelo, temperatura2, calor2
    
if __name__ == "__main__":

    modelo, temperatura2, calor2 = predict()
    
    # Evaluar el modelo y realizando las metricas mas relevantes
    
    vectorcalorpredicho = modelo.predict(temperatura2.reshape((-1, 1)))
    error = calor2 - vectorcalorpredicho
    error_MSE = np.mean((calor2 - vectorcalorpredicho) ** 2)
    
    #print(modelo.predict(np.array([[0.28]]))) para un solo dato 
    
    print('Prediccion (°C):',vectorcalorpredicho * 100)
    print('Error:', error * 100)
    print('Error cuadratico medio:',error_MSE * 100)
    #print(temperatura2)
    
    # Coeficiente de determinación R^2 1 para indicar que se ajusta adecuadamente,0 caso contrario
    
    r2 = modelo.score(temperatura2, calor2)
    print('Coeficiente de determinación (R^2):', r2)
    
    # Predicciones para nuevas temperaturas en caso de que sean lineales o equidistantes
    
    # nuevas_temperaturas = np.array([24, 25, 26]).reshape((-1, 1)) / 100.0
    # nuevas_predicciones = modelo.predict(nuevas_temperaturas)
    # print('Predicciones para nuevas temperaturas (°C):', nuevas_predicciones*100)
    
    # Visualización
    
    plt.xlabel('Temperatura')
    plt.ylabel('Calor')
    plt.title('Grafico datos + Linea de regresion')
    plt.scatter(temperatura2*100, calor2*100, color='blue')
    plt.plot(temperatura2*100, vectorcalorpredicho*100, color='red')
    plt.show()
    