# Resultados Climatización #

## Tabla ##

La siguiente tabla consigna los valores para la variable calor desarrollados por ***Climatizacion55NN.R***, aqui se muestran los valores relevantes por cada tipo de red, capas y nodos; luego tenga en cuenta que los valores de peso son de caracter aleatorio y no es recomendable dejarlos fijos para este tipo de prácticas (la entrada es 26°C o .26 normalizada, tal y como se plantea en el codigo con el dataframe y no el archivo.csv). 

**Recomendaciones**

1. Amplie el dataframe o generelo con otras herramientas, tenga en cuenta el procesamiento y desarrolle un filtro de elementos vacios por cada iteración
2. Compare los resultados obtenidos con este y otros enfoques desarrollados en el directorio principal, para realizar sus propias conjeturas
3. Estos datos se obtuvieron con la herramienta Rcommander, tenga esto en cuenta cuando quiera realizar una migración de la alternativa
4. Recuerde que al ser el resultado una "predicción" esta sujeta a una incertidumbre, por ende establecer un rango o comparación entre enfoques le permitira entre otras cosas determinar cual es el valor mas adecuado para desarrollar su controlador...  

| No. de Capas | No. de Nodos | Temperatura a predecir °C | Temperatura predicha °C |
| --- | --- | --- | --- | 
| 2 capas | 2 Nodos | 26 | 40.18 |
| 2 capas | 2 Nodos | 26 | 40.06 |
| 2 capas | 3 Nodos | 26 | 39.54 |
| 2 capas | 3 Nodos | 26 | 39.11 |
| 2 capas | 4 Nodos | 26 | 39.96 |
| 2 capas | 4 Nodos | 26 | 40.34 |
| 2 capas | 5 Nodos | 26 | 40.39 |
| 2 capas | 5 Nodos | 26 | 39.66 |
| 3 capas | 2 Nodos | 26 | 39.71 |
| 3 capas | 2 Nodos | 26 | 39.86 |
| 3 capas | 3 Nodos | 26 | 40.71 |
| 3 capas | 3 Nodos | 26 | 39.28 |
| 3 capas | 4 Nodos | 26 | 40.75 |
| 3 capas | 4 Nodos | 26 | 39.78 |
| 3 capas | 5 Nodos | 26 | 40.40 |
| 3 capas | 5 Nodos | 26 | 40.40 |

**Notas** 

- Recuerde que al obtener estos datos, se tiende a calcular una media para aproximar el valor "real", no obstante este hecho asume que los errores son simetricos y se "cancelan" entre si lo cual puede no ser cierto
- Luego esto no quiere decir que no pueda restringir el valor real a un rango, para utilizarlos como base a otros posibles enfoques y tecnicas para mejorar el rendimiento de su controlador
- Más que comparar capas o cantidad de nodos es conocer la naturaleza de los datos. Entender la naturaleza de los datos es fundamental para cualquier tipo de modelado. Esto incluye entender la distribución de los datos, las relaciones entre las variables, y cualquier posible sesgo o anomalía.

## Consola R Commander ##

El siguiente es un modelo sencilo de arbol desarrollado en R, se obtuvo con el archivo de instrucciones **Modelo_sencillo_arbol.R** y sus salidas representativas son 

```
n= 6 

node), split, n, deviance, yval
      * denotes terminal node

1) root 6 333.3333 28.33333 *
```
```
> print(prediccion)
[1] 28.33333
```
Esta salida en R Commander significa que ha realizado un analisis de arboles de decision (DT) con 6 observaciones n = 6. El arbol tiene un nodo raiz y un nodo terminal marcado con un asterisco (*) lo que indica que es un nodo terminal o hoja

El primer nodo, el nodo raiz tiene 6 casos (n = 6) y una desviación cuadratica (deviance) de 333.3333 y un valor de validación (yval). Para este caso el hecho de que tenga un solo nodo terminal significa que no se ha dividido mas alla de este. Esto podria sugerrir que el modelo de arbol no ha logrado encontar suficiente variabilidad o diferencias significativas en los datos para crear mas nodos.

El segundo nodo, el nodo terminal, tambien tiene 6 casos (n = 6) y una desviación cuadratica de 28.333 esto significa que el nodo terminal es mas preciso que el nodo raiz ya que la desviación cuadratica es menor

___Conclusión___

El comportamiento parece inesperado y no esta ajustado correctamente a los cambios de temperatura. El hecho de que la predicción de calor siga siendo 28.33. Indica qeu el modelo de arbol puede no estar funcionando correctamente o puede estar careciendo de adecuada capacidad pra predecir la variable "calor" en funcion de la variable "temperatura" 

Producto de esta carencia, se extendio el conjunto de datos a utilizar en **Modelo_sencillo_arbolexp.R** 

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

English 

## Air conditioning results ##

## Table ##

The following table shows the values for the heat variable developed by ***Climatizacion55NNN.R***, here are the relevant values for each type of network, layers and nodes; then note that the weight values are of random character and it is not recommended to leave them fixed for this type of practices (the input is 26°C or .26 normalized, as stated in the code with the dataframe and not the .csv file).

**Recommendations**

1. Extend the dataframe or generate it with other tools, take into account the processing and develop a filter of empty elements for each iteration.
2. Compare the results obtained with this and other approaches developed in the main directory, to make your own conjectures.
3. These data were obtained with the Rcommander tool, keep this in mind when you want to perform a migration of the alternative.
4. Remember that as the result is a "prediction" it is subject to uncertainty, therefore establishing a range or comparison between approaches will allow you, among other things, to determine which is the most appropriate value to develop your controller...

| N. of layers | N. de Nodes | Temperature to predict °C | Temperature predicted °C |
| --- | --- | --- | --- | 
| 2 layers | 2 Nodes | 26 | 40.18 |
| 2 layers | 2 Nodes | 26 | 40.06 |
| 2 layers | 3 Nodes | 26 | 39.54 |
| 2 layers | 3 Nodes | 26 | 39.11 |
| 2 layers | 4 Nodes | 26 | 39.96 |
| 2 layers | 4 Nodes | 26 | 40.34 |
| 2 layers | 5 Nodes | 26 | 40.39 |
| 2 layers | 5 Nodes | 26 | 39.66 |
| 3 layers | 2 Nodes | 26 | 39.71 |
| 3 layers | 2 Nodes | 26 | 39.86 |
| 3 layers | 3 Nodes | 26 | 40.71 |
| 3 layers | 3 Nodes | 26 | 39.28 |
| 3 layers | 4 Nodes | 26 | 40.75 |
| 3 layers | 4 Nodes | 26 | 39.78 |
| 3 layers | 5 Nodes | 26 | 40.40 |
| 3 layers | 5 Nodes | 26 | 40.40 |

**Notes**. 

- Remember that when you get this data, you tend to calculate an average to approximate the "real" value, however this assumes that the errors are symmetrical and "cancel" each other which may not be true.
- So this does not mean that you cannot restrict the true value to a range, to use as a basis for other possible approaches and techniques to improve the performance of your controller.
- More than comparing layers or number of nodes is knowing the nature of the data. Understanding the nature of the data is fundamental to any type of modeling. This includes understanding the distribution of the data, the relationships between variables, and any possible biases or anomalies.










