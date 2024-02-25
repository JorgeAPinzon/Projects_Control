**INTRODUCCION** 

El siguiente proyecto pretende tener un enfoque o aproximar lo que seria un control inteligente para un sistema de climatización, que resumiendo no es más que garantizar
unas condiciones de temperatura y calidad de aire en un medio normalmente confinado (ver documentación adjunta); entonces este tipo de sistemas son ampliamente utilizados
para el bienestar y confort de las personas. 

**ESTRUCTURA**

Para comenzar lo primero que tiene que tener en cuenta es el orden de comprensión del proyecto en base a los archivos..., ya que esto le permitirá diferenciar entre una
alternativa solución y otra
Tal y como lo muestra el presente README 

**ARCHIVOS Y REQUERIMIENTOS**

*fuzzy_climatizacion.py*

Fue desarrollada en el siguiente interprete y contiene las siguientes librerias

- Spyder v 3.3.3 (Linux 32 bits)
- scikit-fuzzy 0.4.2 (comando pip install scikit-fuzzy)
- NumPy (comando pip install numpy)

Este script sencillo toma 3 reglas difusas con sus respectivos conjuntos (ver logica fuzzy), y muestra el comportamiento o sugiere lo que deberia hacer el sistema. 
Asi pues la salida 'calor' se relaciona en función de una entrada 'temperatura' (por defecto a 26 grados), para determinar la forma de la funcion de membresia 
quite los comentarios y deduzca la forma 


*Modelo_precision_simple.py*

Aqui se reliza una "comparación" preliminar utilizando el error cuadrático medio (EMC, es una medida comun de la calidad de un estimador o predictor), solo es una de las
tantas formas en las que se puede realizar dicha comparación; ahora bien notese que se evalua para el mismo conjunto de datos prueba, donde la predicción se realiza 
utilizando regresion lineal 

**SUGERENCIAS**

Nota: Pruebe con conjuntos de datos mas grande y cambie las dimensiones del array, o bien generelos con una funcion aleatoria teniendo en cuenta por supuesto que es un 
proceso de temperatura, en el cual la tasa de cambio puede no ser lo suficientemente rápida en comparación a otro tipo de procesos como control de pocisión, velocidad
angular, radiofrecuencia entre otros sistemas convencionales 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

English Version 

# Introduction

This project aims to focus on or approximate an intelligent control system for an air conditioning unit, which in summary is nothing more than ensuring certain 
temperature and air quality conditions in a confined environment (see attached documentation).

## Structure

To begin, the first thing you should consider is the order of understanding the project based on the files...
As shown in this README.

## Files and Requirements

*fuzzy_climatizacion.py*

This script was developed in the following interpreter and contains the following libraries:

- Spyder v3.3.3 (Linux 32-bit)
- scikit-fuzzy 0.4.2 (Install with `pip install scikit-fuzzy`)
- NumPy (Install with `pip install numpy`)

This simple script uses 3 fuzzy rules with their respective sets (see fuzzy logic), and shows the behavior or suggests what the system should do. 
The output 'heat' is related to an input 'temperature' (default at 26 degrees) to determine the form of the membership function. Remove comments and deduce the form.

*precision_model_simple.py*

In this file, a preliminary "comparison" is made using the mean square error (MSE, a common measure of the quality of an estimator or predictor), it is only one of 
the many ways in which such a comparison can be made. Note that it is evaluated for the same test data set, where the prediction is made using linear regression.

## Suggestions

Note: Try larger data sets, change the dimensions of the array, or generate them with a random function, considering, of course, that it is a temperature process. The rate of change may not be fast enough compared to other types of processes such as position control, speed angular, radio frequency, and other conventional systems.




