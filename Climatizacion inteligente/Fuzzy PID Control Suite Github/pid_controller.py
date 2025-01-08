#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 09:44:05 2024

@author: antiXLinux
"""

import control
import numpy as np
import matplotlib.pyplot as plt
import random

# Datos de entrada son solo una referencia 

temperatura_deseada = 1 # 1 para el error entrada tipo escalon unitario 
temperatura_medida = np.array([26, 27, 28, 29, 30, 31])
calor = np.array([40, 35, 30, 25, 20, 20])

def controlPID():
    """
    .
    Función donde se define y se desarrolla un controlador de temperatura tipo PI

    Returns
    -------
    error_estacionario : TYPE: Numerico 
        DESCRIPTION: Error cuando el valor de la salida ha alcanzado el valor de referencia
    
    risetime : TYPE: Numerico extraido de info
        DESCRIPTION: Tiempo que tarda la señal en cambiar de valor minimo a maximo establecido
    
    settlingtime : TYPE: Numerico extraido de info
        DESCRIPTION: Tiempo de "asentamiento" de la señal 
    
    settlingmin : TYPE: Numerico extraido de info
        DESCRIPTION: Asentamiento minimo (undershoot)
   
    settlingmax : TYPE: Numerico extraido de info
        DESCRIPTION: Asentamiento maximo (overshoot)
    
    overshoot : TYPE: Numerico extraido de info
        DESCRIPTION: Sobreimpulso de la señal con respecto a la referencia
    
    undershoot : TYPE: Numerico extraido de info 
        DESCRIPTION: Fenomeno similar al overshoot en sentido opuesto con respecto al objetivo
    
    t : TYPE: Numerico
        DESCRIPTION: tiempo en segundos
    
    y : TYPE: Numerico
        DESCRIPTION: Representación parcial de la salida
    
    sistema : TYPE: Funcion de transferencia
        DESCRIPTION: Funcion de transferencia para el sistema (hallado con otra herramienta) 
    
    sistema_controlado : TYPE: Producto entre el controlador y sistema
        DESCRIPTION: Control realimentado sin perturbaciones entre los bloques del sistema

    """
    # Crear el modelo del sistema y extraer la funcion de transferencia (usada otra herramienta)
    
    sistema = control.tf([-6.226, -18.29, -16.08, -8.816], [1, -0.8192, 0.5034, 0.2201])
    
    # Crear el controlador PI
    
    kp = 8
    ki = 0.19
    kd = 1
    
    controlador = control.tf([kp, ki], [1, 0])
    
    #controlador = control.tf([kp, ki,kd], [1, 0]) agrega variable derivativa el 1,0 es el grado 
    #del denominador 
    
    # Conectar el controlador al sistema
    
    sistema_controlado = control.feedback(controlador * sistema)
    
    # Calcular la respuesta a una señal tipo paso unitario
    
    t, y = control.step_response(sistema_controlado)

    # Obtener las métricas de la respuesta al escalón
    
    info = control.step_info(sistema_controlado)
    
    # Calcular los valores por aparte si se desea obtener informacion del controlador 
    
    risetime = info['RiseTime']
    settlingtime = info['SettlingTime']
    settlingmin = info['SettlingMin']
    settlingmax = info['SettlingMax']
    overshoot = info['Overshoot']
    undershoot = info['Undershoot']

    # Calcular el error de estado estacionario iniclamente con una entrada tipo escalon unitario 
    
    error_estacionario = temperatura_deseada - y[-1]
    
    
    return  (error_estacionario, risetime, settlingtime, settlingmin, settlingmax,
              overshoot, undershoot, t, y, sistema, sistema_controlado)

    
if __name__ == "__main__":
    
    
    #forma adecuada de llamar los valores que necesita no es posible con info (tipo de dato) 
    
    (error_estacionario , risetime, settlingtime, settlingmin, settlingmax,
     overshoot, undershoot, t, y, sistema, sistema_controlado) = controlPID()
    
    
    print(f"Error de estado estacionario: {error_estacionario}")
    
    # obteniendo los info respuesta al paso
    
    print("Información de la respuesta al escalón:")
    print(f"RiseTime: {risetime}")
    print(f"SettlingTime: {settlingtime}")
    print(f"SettlingMin: {settlingmin}")
    print(f"SettlingMax: {settlingmax}")
    print(f"Overshoot: {overshoot}")
    print(f"Undershoot: {undershoot}")
    
    # Graficar la respuesta
    
    plt.plot(t, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Temperatura')
    plt.title('Respuesta a una señal tipo paso unitario')
    plt.grid(True)
    plt.show()
    
    
    desired_values = [40, 45, 50, 55, 60];
    
    # Para cada valor deseado... y calculo del error del estado estacionario
    
    for i in range(len(desired_values)):
        
        # Establece el valor deseado actual
        
        desired_value = desired_values[i]

        # Calcula la respuesta del sistema a una entrada constante del valor deseado
        
        t, y = control.step_response(desired_value * sistema_controlado)
        
        # El valor final de la respuesta del sistema es el último valor de y
        
        final_value = y[-1]

        # El error de estado estacionario es la diferencia entre el valor deseado y el valor final
        
        steady_state_error = desired_value - final_value

        # Imprime el error de estado estacionario
        
        print(f'Para un valor deseado de {desired_value}, el error de estado estacionario es {steady_state_error}')
        


    
    
    
    
    
