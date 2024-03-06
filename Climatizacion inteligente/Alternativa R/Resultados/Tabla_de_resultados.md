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

Producto de esta carencia, se extendio el conjunto de datos a utilizar en **Modelo_sencillo_arbolexp.R** donde las salidas mas relevantes son: 
```
n= 31 

node), split, n, deviance, yval
      * denotes terminal node

1) root 31 1209.6770 26.45161  
  2) temperatura>=28.5 18  100.0000 21.66667 *
  3) temperatura< 28.5 13  126.9231 33.07692 *

> prediccion <- predict(modelo_arbol, newdata = data.frame(temperatura = 26))

> print(prediccion)
       1 
33.07692
```
- Ahora bien aqui el numero de observaciones es 31, la desviacion es de 1209.6770 y un valor promedio de la variable "calor" de 26.45161. 

- La linea 2) temperatura>=28.5 18  100.0000 21.66667 * , siendo un nodo terminal indica que para las observaciones donde "temperatura" es mayor o igual a 28.5 hay 18 observaciones una desviacion de 100.000 y un valor promedio de "calor" de 21.66667

- La linea 3 3) temperatura< 28.5 13  126.9231 33.07692 * este nodo terminal indica que para las observaciones donde "temperatura" es menor a 28.5 hay 13 observaciones una desviación de 126.9231 y un valor promedio de "calor" de 33.07692

___Conclusión___

En cuanto a la precisión de las predicciones es cierto que a medida que se tienen mas datos y mas variabilidad presenten, las prediciones seran mas precisas. Esto se debe a que el modelo tiene mas información para aprender de los datos; sin embargo depende tambien del modelo y de la variabilidad de los datos. Por lo tanto siempre es importante evaluar la precision de tus predicciones utilizando tecnicas de validación cruzadas o conjuntos de prueba separados.

Ademas de clasificar o "filtrar" los datos otras posibles aplicaciones serian: 

1. Identificacion de umbrales criticos: Los arboles de decision identifican umbrales en las variables de entrada que resultan en cambios significativos en la variable de la salida.(28.5°C para 31 observaciones)
2. Analisis de sensibilidad: Se puede utlizar el modelo para entender como cambia la predicción del calor en respuesta de cambios de temperatura. Asi entendiendo dicha relación se pueden realizar ajustes (tenga en cuenta que esto se da en terminos del comportamiento del modelo, no de los datos)
3. Por ultimo estan las medidas para reducir el calor definido mas como una de las estrategias de aplicacion no de modo

Por ultimo esta incluido el conjunto de instrucciones llamado **Clustering_climatizacion.R** obtenido con **Guia R clustering Climatizacion**, que hace referencia al agrupamiento de datos de entrada, y la declaración de un vector predicción, son obtenidas metricas para determinar la referencia al cluster por cada dato de entrada-salida importado (importante cargarlo desde el menu importar datos .csv o dataframe), con este vector de pertenencia es posible obtener el grafico_sencillo_clustering (direcctorio resultados) e imprimir en consola los datos predichos con respecto a ```nuevos_datos <- data.frame(temperatura = c(26, 27, 28, 29, 30, 31))```; regresion lineal solo como una referente. Luego los datos mas relevantes de este desarrollo se pueden ver a continuación:
```
> with(Dataset, stem.leaf(calor, na.rm=TRUE))
1 | 2: represents 12
 leaf unit: 1
            n: 6
   2    2* | 00
  (1)   2. | 5
  (1)   3* | 0
   2    3. | 5
   1    4* | 0
```
leaf unit : hace referencia a que la unidad de hojas es 1
n = 6 : numero de observaciones 
 2    2* | 00 : Esto representa el numero 20 en los datos por ejemplo y la primera cifra hace alusion a la frecuencia 

```
 > print(kmeans_resultado)
K-means clustering with 2 clusters of sizes 3, 3

Cluster means:
  temperatura    calor
1          27 35.00000
2          30 21.66667

Clustering vector:
[1] 1 1 1 2 2 2

Within cluster sum of squares by cluster:
[1] 52.00000 18.66667
 (between_SS / total_SS =  79.9 %)

Available components:

[1] "cluster"      "centers"      "totss"        "withinss"     "tot.withinss" "betweenss"    "size"         "iter"         "ifault"
```
Gráfico con puntos negro y rojo para la pertenencia de los cluster es decir: 

Cluster means: Son los centros de los clusters. En este caso, el primer cluster tiene un promedio de temperatura de 27 y un promedio de calor de 35. El segundo cluster tiene un promedio de temperatura de 30 y un promedio de calor de 21.67.

Clustering vector: Indica a qué cluster pertenece cada observación. Para este caso las primeras tres observaciones pertenecen al primer cluster y las últimas tres al segundo cluster.

Within cluster sum of squares by cluster: Es la suma de las distancias al cuadrado de cada punto a su centroide. Cuanto menor sea este valor, más “compacto” es el cluster.

(between_SS / total_SS = 79.9 %): Esta es una medida de cuánta variación se explica por los clusters. Entonces el 79.9% de la variación en los datos se explica por la pertenencia a los clusters.

El modelo 3 se compone internamente:
```
Call:
lm(formula = calor ~ temperatura, data = Dataset)

Residuals:
      1       2       3       4       5       6 
 0.9524  0.2381 -0.4762 -1.1905 -1.9048  2.3810 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 150.4762    11.7743   12.78 0.000216 ***
temperatura  -4.2857     0.4124  -10.39 0.000484 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 1.725 on 4 degrees of freedom
Multiple R-squared:  0.9643,	Adjusted R-squared:  0.9554 
F-statistic:   108 on 1 and 4 DF,  p-value: 0.0004841
```
Y el vector predicciones es:
```
> print(predicciones)
       1        2        3        4        5        6 
39.04762 34.76190 30.47619 26.19048 21.90476 17.61905
```


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


## R Commander Console ##

following is a simple tree model developed in R, it was obtained with the instructions file **Modelo_sencillo_arbol.R** and its representative outputs are

```
n= 6

node), split, n, deviance, yval
       * denotes terminal node

1) root 6 333.3333 28.33333 *
```
```
> print(prediction)
[1] 28.33333
```
This output in R Commander means that you have performed a decision tree (DT) analysis with 6 observations n = 6. The tree has a root node and a terminal node marked with an asterisk (*) indicating that it is a terminal node or sheet

At first node, the root node, has 6 cases (n = 6) and a quadratic deviation (deviance) of 333.3333 and a validation value (yval). In this case, the fact that it has a single terminal node means that it has not been divided beyond this one. This could suggest that the tree model has failed to find enough variability or significant differences in the data to create more nodes.

The second node, the terminal node, also has 6 cases (n = 6) and a quadratic deviation of 28,333. This means that the terminal node is more accurate than the root node since the quadratic deviation is smaller.

___Conclusion___

behavior seems unexpected and is not adjusted correctly to temperature changes. The fact that the heat prediction is still 28.33. Indicates that the tree model may not be working correctly or may be lacking adequate capacity to predict the variable "heat" as a function of the variable "temperature"

As a result of this lack, the data set to be used in **Modelo_sencillo_arbolexp.R** was extended where the most relevant outputs are:

```
n= 31 

node), split, n, deviance, yval
      * denotes terminal node

1) root 31 1209.6770 26.45161  
  2) temperatura>=28.5 18  100.0000 21.66667 *
  3) temperatura< 28.5 13  126.9231 33.07692 *

> prediccion <- predict(modelo_arbol, newdata = data.frame(temperatura = 26))

> print(prediccion)
       1 
33.07692
```
- Now here the number of observations is 31, the deviation is 1209.6770 and an average value of the "calor" variable is 26.45161.

- Line 2) temperatura>=28.5 18 100.0000 21.66667 *, being a terminal node indicates that for observations where "temperatura" is greater than or equal to 28.5 there are 18 observations a deviation of 100.000 and an average value of "calor" of 21.66667

- Line 3 3) temperatura < 28.5 13 126.9231 33.07692 * this terminal node indicates that for observations where "temperatura" is less than 28.5 there are 13 observations a deviation of 126.9231 and an average value of "calor" of 33.07692

___Conclusion___

Regarding the precision of the predictions, it is true that as more data is available and more variability is present, the predictions will be more precise. This is because the model has more information to learn from the data; However, it also depends on the model and the variability of the data. Therefore it is always important to evaluate the accuracy of your predictions using cross-validation techniques or separate test sets.

In addition to classifying or "filtering" the data, other possible applications would be:

1. Identification of critical thresholds: Decision trees identify thresholds in the input variables that result in significant changes in the output variable (28.5°C for 31 observations)
2. Sensitivity analysis: The model can be used to understand how the heat prediction changes in response to temperature changes. By understanding this relationship, adjustments can be made (note that this is in terms of the behavior of the model, not the data).
3. Finally, there are measures to reduce heat defined more as one of the application strategies, not in a way

Finally, the set of instructions called **Clustering_climatizacion.R** is included, obtained with **Guia R clustering Climatizacion**, which refers to the grouping of input data, and the declaration of a prediction vector, metrics are obtained to determine the reference to the cluster for each imported input-output data (it is important to load it from the import data .csv or dataframe menu), with this membership vector it is possible to obtain the simple_clustering graph (results directory) and print the predicted data with respect to the console ```new_data <- data.frame(temperature = c(26, 27, 28, 29, 30, 31))```; Linear regression only as a reference. Then the most relevant data of this development can be seen below:
```
> with(Dataset, stem.leaf(calor, na.rm=TRUE))
1 | 2: represents 12
 leaf unit: 1
            n: 6
   2    2* | 00
  (1)   2. | 5
  (1)   3* | 0
   2    3. | 5
   1    4* | 0
```
leaf unit: refers to the leaf unit being 1
n = 6: number of observations
  2 2* | 00: This represents the number 20 in the data for example and the first figure refers to the frequency
```
 > print(kmeans_resultado)
K-means clustering with 2 clusters of sizes 3, 3

Cluster means:
  temperatura    calor
1          27 35.00000
2          30 21.66667

Clustering vector:
[1] 1 1 1 2 2 2

Within cluster sum of squares by cluster:
[1] 52.00000 18.66667
 (between_SS / total_SS =  79.9 %)

Available components:

[1] "cluster"      "centers"      "totss"        "withinss"     "tot.withinss" "betweenss"    "size"         "iter"         "ifault"
```
Graph with black and red points for the cluster membership, that is:

Cluster means: They are the centers of the clusters. In this case, the first cluster has an average temperature of 27 and an average heat of 35. The second cluster has an average temperature of 30 and an average heat of 21.67.

Vector clustering: Indicates which cluster each observation belongs to. In this case, the first three observations belong to the first cluster and the last three to the second cluster.

Within cluster sum of squares by cluster: It is the sum of the squared distances of each point to its centroid. The lower this value is, the more “compact” the cluster is.

(between_SS / total_SS = 79.9%): This is a measure of how much variation is explained by the clusters. Then 79.9% of the variation in the data is explained by cluster membership.

Model 3 is internally composed:

```
Call:
lm(formula = calor ~ temperatura, data = Dataset)

Residuals:
      1       2       3       4       5       6 
 0.9524  0.2381 -0.4762 -1.1905 -1.9048  2.3810 

Coefficients:
            Estimate Std. Error t value Pr(>|t|)    
(Intercept) 150.4762    11.7743   12.78 0.000216 ***
temperatura  -4.2857     0.4124  -10.39 0.000484 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 1.725 on 4 degrees of freedom
Multiple R-squared:  0.9643,	Adjusted R-squared:  0.9554 
F-statistic:   108 on 1 and 4 DF,  p-value: 0.0004841
```
and prediction vector is :
```
> print(predicciones)
       1        2        3        4        5        6 
39.04762 34.76190 30.47619 26.19048 21.90476 17.61905




