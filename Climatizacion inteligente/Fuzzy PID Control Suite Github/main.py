#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:27:15 2024

@author: antiXLinux
"""

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import control
import matplotlib.pyplot as plt
import random
from simple_model import predict
from fuzzy_logic import fuzzy
from fuzzy_logic import evaluar_temperatura
from pid_controller import controlPID
import gui
import time


def main():
    """
    .
    Función main cabecera de todos los scripts y herramientas importadas
    
    Returns
    -------
    e : TYPE Numerico
        DESCRIPTION: Error cuando el valor de la salida ha alcanzado el valor de referencia
    
    tr : TYPE Numerico risetime
        DESCRIPTION: Tiempo que tarda la señal en cambiar de valor minimo a maximo establecido
    
    ts : TYPE Numerico
        DESCRIPTION: Tiempo de asentamiento de la señal 
    
    Mp : TYPE Numerico 
        DESCRIPTION: Sobreimpulso de la señal con respecto a la referencia
        
    settlingmin : TYPE Numerico
        DESCRIPTION.Asentamiento minimo (undershoot)
        
    settlingmax : TYPE Numerico 
        DESCRIPTION. Asentamiento maximo (overshoot)
        
    overshoot : TYPE Numerico
        DESCRIPTION: Sobreimpulso de la señal con respecto a la referencia
        
    undershoot : TYPE Numerico
        DESCRIPTION: Fenomeno similar al overshoot en sentido opuesto con respecto al objetivo

    """
    
    
    # Control de acceso usuarios autorizados
    
    authorized_users = {
        
    "admin": "admin",
    "user1": "jk612aLp",
    "user2": "tester"
    
    }

    def login():
        
        """Función para autenticar al usuario"""
        
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    # Verifica si el usuario está autorizado
    
    if username in authorized_users and authorized_users[username] == password:
        
        print("Acceso concedido. Bienvenido,", username)
        #logica de funciones o items de acceso predeterminado la ejecucion completa
        
    else:
        
        print("Nombre de usuario o contraseña incorrectos.")
        
        while True:
            
            print("Acceso denegado, reinicie la aplicación...")


    # Llamar a la función de inicio de sesión
    
    login()
    
    # parte de predicción o modelo de regresion 
    
    modelo,temperatura,calor = predict()
    
    print("\nModo preprocesamiento...\n")
    
    app = gui.Guiv1App() # referencia de la aplicacion y eventos,atributos .____ event()
    
    # Evaluar el modelo y realizando las metricas mas relevantes
    
    vectorcalorpredicho = modelo.predict(temperatura.reshape((-1, 1)))
    error = calor - vectorcalorpredicho
    error_MSE = np.mean((calor - vectorcalorpredicho) ** 2)
    
    #print(modelo.predict(np.array([[0.28]]))) para un solo dato 
    
            
# Llama a la función para comenzar la actualización continua
       
    print('Prediccion (°C):',vectorcalorpredicho * 100)
    print('Error:', error * 100)
    print('Error cuadratico medio:',error_MSE * 100)
    r2 = modelo.score(temperatura, calor)
    print('Coeficiente de determinación (R^2):', r2)
    
    # Visualización
        
    plt.xlabel('Temperatura')
    plt.ylabel('Calor')
    plt.title('Grafico datos + Linea de regresion')
    plt.scatter(temperatura*100, calor*100, color='blue')
    plt.plot(temperatura*100, vectorcalorpredicho*100, color='red')
    plt.show()
    
    
    #app.run() hasta aca opera el modo regresion lineal
    
    # parte fuzzy 
    
    sistemaf = fuzzy()
    
    print("\nFuzzy aplicado a las entradas")
    
    # Contador para los valores considerados frios, comodos, calientes
    # Cargar la imagen capturada
    
    contador = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    activacion_ruido = 0
        
    # Lista y amplitudes para almacenar los valores considerados frios, comodos, calientes
    # Semiautomatico y automatico
    
    valores = []
    Amplitud1 = 1
    valores2 = []
    Amplitud2 = 1
    Amplitud21 = 1
    valores3 = []
    Amplitud3 = 1
    valores4 = [] # atipicos para calor extremo no clima
    Amplitud4 = 1
    valores5 = [] # atipicos para '''
    valores6 = []
    Amplitudinter = 1
    
    #fuzzy + Entradas para PI

    for i in range(len(temperatura)):
            
        temp = temperatura[i][0] * 100  # Accede al valor escalar y conviértelo a la escala original
        valor_calor_fuzzy = evaluar_temperatura(sistemaf, temp)
        #app.text1.insert("1.0", valor_calor_fuzzy) # fuzzy a las salidas calor fuzzy.py
        activacion_ruido = 1    
        # Verifica valores de acuerdo a pertenencia difusa
        
        if 60.51 < valor_calor_fuzzy < 82.77:
            
                #contador += 1
                valores.append(temp) # Agrega el valor a la lista
                
                if len(valores) > 2 and all(temp >= 4 for temp in valores[-3:]):
                    Amplitud1 = 16

                # Verifica si el siguiente valor está en el mismo rango
                if i < len(temperatura) - 1:
                    
                    activacion_ruido = 0
                    contador+=1
                
        elif 49.73 < valor_calor_fuzzy < 50.28:
            
            #contador2 += 1
            valores2.append(temp)
            
            if len(valores2) > 2 and all(temp >= 18 for temp in valores2[-3:]):
                Amplitud2 = 21

            if i < len(temperatura) - 1:
                
                activacion_ruido = 0
                contador2+=1
            
        elif 44.18 < valor_calor_fuzzy < 49.6:
            
            #contador3 += 1
            valores3.append(temp)
            
            if len(valores3) > 2 and all(temp >= 24 for temp in valores3[-3:]):
                Amplitud3 = 22

            if i < len(temperatura) - 1:
                
                activacion_ruido = 0
                contador3+=1
            
        elif 44.18 > valor_calor_fuzzy:
            
            #contador4 += 1
            valores4.append(temp)
            
            if len(valores4) > 2 and all(temp > 28 for temp in valores4[-3:]):
                Amplitud4 = 26
                
            if i < len(temperatura) - 1:
                
                activacion_ruido = 0
                contador4+=1
            
        elif 82.97 < valor_calor_fuzzy:
            
            #contador5 += 1
            valores5.append(temp)
            
            if len(valores5) > 2 and all(temp < 4 for temp in valores5[-3:]):
                Amplitud5 = 4
            
            if i < len(temperatura) - 1:
                
                activacion_ruido = 0
                contador5+=1
                
        elif 50.58 < valor_calor_fuzzy < 55.34:  # intermedios en el limbo
            
            #contador6 += 1
            valores6.append(temp)
            
            if len(valores6) > 2 and all(temp >= 13 for temp in valores6[-3:]):
                Amplitudinter = 15
            
            if i < len(temperatura) - 1:
                
                activacion_ruido = 0
                contador6+=1
        
    # Imprime el número de valores en el rango 
    
    print(f"\nNúmero de valores menores a 4: {contador5}")     
    print(f"Número de valores entre 4 y 12: {contador}")
    print(f"Número de valores entre 18 y 23: {contador2}")
    print(f"Número de valores entre 24 y 28: {contador3}")  
    print(f"Número de valores mayores a 28: {contador4}") 
   
    #Imprime los valores en el rango 
    
    print(f"\nTemperaturas fuzzy menores a 4: {valores5}")    
    print(f"Temperaturas fuzzy entre 4 y 12: {valores}")
    print(f"Temperaturas fuzzy entre entre 18 y 23: {valores2}")
    print(f"Temperaturas fuzzy entre entre 24 y 28: {valores3}")
    print(f"Temperaturas fuzzy  mayores a 28: {valores4}") 
    
    
    # print("\nFuzzy aplicado a las predicciones")
    
    # for temp in vectorcalorpredicho:
        
    #     evaluar_temperatura(sistemaf, temp * 100)
        
    # parte del controlador
    
    (error_estacionario , risetime, settlingtime, settlingmin, settlingmax,
     overshoot, undershoot, t, y, sistema, sistema_controlado) = controlPID()
    
    # Prueba tipos de entrada  

    # Creando un vector de tiempo

    tiempo = np.linspace(0, 10, 227)
    
    # Identificacion de datos y crear alternativas a las señales de entrada
    
    if contador >=2 and temp <=12:
        
        activacion_ruido = 0
        entrada_paso =Amplitud1*np.ones_like(tiempo) # para generar amplitud entrada_paso_50 = 50 * np.ones_like(tiempo)
        
    if contador2 >=2 and temp <=24:
        
        activacion_ruido = 0    
        entrada_paso =Amplitud2*np.ones_like(tiempo)
        
    if contador3 >=2 and temp <=28.1: # 28.1 por flotante 0.000000004 aprox
    
        activacion_ruido = 0    
        entrada_paso =Amplitud3*np.ones_like(tiempo)
        
    if contador3 >=2 and temp <=30: # agregado para rango
    
        activacion_ruido = 0    
        entrada_paso =Amplitud3*np.ones_like(tiempo)
        
    if contador4 >=2 and temp > 28:
        
        activacion_ruido = 0    
        entrada_paso =Amplitud4*np.ones_like(tiempo)
        
    if contador5 >=2 and temp <= 4:
        
        activacion_ruido = 0   
        entrada_paso =Amplitud5*np.ones_like(tiempo)
              
    elif contador6 >=2 and temp <= 18:
        
        activacion_ruido = 0    
        entrada_paso = Amplitudinter*np.ones_like(tiempo)
    
    elif temp<=7 and contador>0: 
        
        activacion_ruido = 0
        entrada_paso = temp*np.ones_like(tiempo)
        
    
    # Manejo del ruido y suavizado x promedio en algunos casos 
    
    if (contador <= 1 and contador2 <= 1 and contador3 <= 1  
        
        and contador4 <= 1 and contador5 <= 1 and contador6 <= 1): 
        
        entrada_paso = temp*np.ones_like(tiempo)
        
    contadores = [contador, contador2, contador3, contador4, contador5, contador6]
    valores_mayores_igual_2 = [c for c in contadores if c >= 2]
    valores_tomados = [c for c in temperatura if c <= 0.42] # por arriba del maximo Col sin HR OjO
    valores_descartados = [c for c in temperatura if c >= 0.43]
    #print(f'\nValores descartados {valores_tomados}')
    
    # Promedios
    
    temperaturas_error =sum(valores_tomados) / len(valores_tomados)
   
    if not valores_descartados: # evitando division por 0
        
        temperaturas_error2 = 0
        
    else:
        
        temperaturas_error2 =sum(valores_descartados) / len(valores_descartados)
    
    if len(valores_tomados)>len(valores_descartados) and temperaturas_error2 > temperaturas_error:
        
        activacion_ruido = 1
    
    # segunda etapa de suavizado de la señal
    
    mayor_diferencia = 0
    
    for i in range(1, len(temperatura)):
        
        diferencia = abs(temperatura[i] - temperatura[i-1])
        
        if diferencia > mayor_diferencia:
            
            mayor_diferencia = diferencia

    print("La mayor diferencia entre temperaturas consecutivas es:", mayor_diferencia)
    
    if mayor_diferencia >= 0.10:
        
        activacion_ruido = 1
       
    if any(c >= 2 for c in contadores) and any(c <= 25 for c in valores_mayores_igual_2) and activacion_ruido == 1: 
                                           #any cualquier valor en valores mayores igual a 2
                                           # y cualquiera es menor o igual a 25 entonces:
        
        print('\nMetodo promedio llamado')
        
        temperaturas_error = temperaturas_error*100
        entrada_paso = temperaturas_error*np.ones_like(tiempo)
    
    #entrada_paso =np.ones_like(tiempo)
    entrada_rampa = tiempo
    entrada_impulso = np.zeros_like(tiempo); entrada_impulso[0] = 1
    entrada_senoidal = np.sin(tiempo)
    entradas = [entrada_paso, entrada_rampa, entrada_impulso, entrada_senoidal]
    
    nombres = ['Paso']
    
    #app.run()
    
    
    def calcular_metricas(t, y, entrada):   # parte PI
        
    
        # Calcular el error de estado estacionario
        
        e = abs(y[-1] - entrada[-1])
        
        # Calcular el tiempo de subida (10-90%)
        
        tr_start_index = np.where(y >= 0.1 * y[-1])[0][0]
        tr_end_index = np.where(y >= 0.9 * y[-1])[0][0]
        tr = t[tr_end_index] - t[tr_start_index]
        
        # Calcular el tiempo de asentamiento (2% criterio)
        
        ts_index = np.where(abs(y - y[-1]) > 0.0 * y[-1])[0][-1]
        ts = t[ts_index]
        
        # Calcular el sobreimpulso
        
        Mp = (np.max(y) - y[-1]) / y[-1]
        
        # Calcular el valor mínimo durante el tiempo de asentamiento
        
        settlingmin = np.min(y[ts_index:])
        
        # Calcular el valor máximo durante el tiempo de asentamiento
        
        settlingmax = np.max(y[ts_index:])
        
        # Calcular el overshoot
        
        overshoot = np.max(y) - y[-1]
        
        # Calcular el undershoot
        
        undershoot = y[-1] - np.min(y)
    
        return e, tr, ts, Mp, settlingmin, settlingmax, overshoot, undershoot
    
    
    for entrada, nombre in zip(entradas, nombres):
     
     # Calcular la respuesta del sistema
     
     respuesta= control.forced_response(sistema_controlado, tiempo, entrada)
     
     # Desempaquetar los valores devueltos
     
     tiempo_respuesta, y_respuesta = respuesta
     
     # Calcular las métricas
     
     (e, tr, ts, Mp, settlingmin, settlingmax, 
      overshoot, undershoot) = calcular_metricas(tiempo_respuesta, y_respuesta, entrada)
     
     # Calcular el error de estado estacionario
     
     e = abs(y_respuesta[-1] - entrada[-1])
 
     # Imprimir las métricas
     
     print(f'\nPara una entrada {nombre}:')
     print(f'Error de estado estacionario: {e}')
     print(f'Tiempo de subida: {tr} s')
     print(f'Tiempo de asentamiento: {ts} s')
     print(f'Sobreimpulso: {Mp * 100} %')
     print(f'Valor mínimo durante el tiempo de asentamiento: {settlingmin}')
     print(f'Valor máximo durante el tiempo de asentamiento: {settlingmax}')
     print(f'Overshoot: {overshoot}')
     print(f'Undershoot: {undershoot}')
     
   # Graficar la respuesta
        
     #plt.figure()
     plt.plot(tiempo_respuesta, y_respuesta)
     plt.title(f'Respuesta al escalon para una entrada {nombre}')
     plt.xlabel('Tiempo (s)')
     plt.ylabel('Amplitud')
     plt.grid(True)
     plt.show()
     
     app.run()
     
     
if __name__ == "__main__":
    
    main()