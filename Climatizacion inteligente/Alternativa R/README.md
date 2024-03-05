# Alternativa R-Rcommander #

## Resumen ##

Las tecnologías de refrigeración generalmente se dividen en aplicaciones de climatización (air conditioning) y refrigeración, Las tecnologías de aire acondicionado se 
definen como aquellas que se utilizan para mantener condiciones de confort térmico aceptables para personas y equipos en edificios y espacios residenciales, comerciales 
e industriales, típicamente en un entorno que esta entre 20° y 30°. 

Esta alternativa explora R-Rcommander donde **Climatizacion55NN.R** genera los resultados (carpeta en el directorio), creando una red neuronal y una predicción en base a 
los datos normalizados de entrada (**Datos_temperatura_climatizacion.csv**), muestra como varia el "calor" en funcion de una temperatura dada, mostrandolo en un grafico 
junto con la predicción en la iteración correspondiente (deseada ver Resultados/Tabla_de_resultados.md)

Por su parte el archivo **Modelo_sencillo_arbol.R** que a diferencia de la red neuronal no se necesitan normalizar los datos, se "carga" el dataframe propuesto en el directorio (n = 6 observaciones). Sin embargo revela resultados desalentadores incialmente, pero a manera conceptual interesantes, debido a la capacidad de segmentar y clasificar los datos incluso con una predicción no muy buena. Entre las alternativas solución se encuentran:

1. Verificar el conjunto de datos en busqueda de lecturas erroneas, espacios por iteración entre otros
2. Revisar y limpiar el historico de datos o cualquier referente al preprocesamiento (si lo hubo)
3. Analizar y recomprender el modelo del arbol
4. El conjunto de datos es tan pequeño que no presenta una variabilidad significativa
5. Intentar mejorar el modelo del arbol, por ejemplo ajustando los parametros de crecimiento del arbol; intentar diferentes enfoques de modelo o considerando otros tipos de modelos estadisticos que puedan ser mas adecuados para este conjunto de datos

Luego es importante tener en cuenta que el analisis y la interpretación de los modelos pueden ser complejos, y requieren varias iteraciones; es precisamente la prueba que se realiza en **Modelo_sencillo_arbolexp** aumentando la cantidad de datos con el fin de obtener resultados mas precisos y utiles.

Por ultimo utilizando el archivo **Guia R clustering Climatizacion**, se creo conjunto de instrucciones **Clustering_climatizacion.R** con un dataframe auxiliar, para realizar el vector predicciones, una vez importado el archivo .csv (en este directorio) es realizado el agrupamiento en base a los centros y calculo de distancias. Despues con el vector pertenencia es posible graficar e imprimir en la consola el vector predicciones. Este ultimo se obtuvo utilizando el asistente grafico de la herramienta para regresion lineal (ver en el directorio de Resultados).

## Requerimientos y plataforma de desarrollo ##

Probado y desarrollado en Linux (Debian)

- Instalar dependencias

sudo sed -i.bak "/^#.*deb-src.*universe$/s/^# //g" /etc/apt/sources.list
sudo apt update
sudo apt build-dep r-base

- Para la version 4

curl -O https://cran.rstudio.com/src/base/R-4/R-${R_VERSION}.tar.gz
tar -xzvf R-${R_VERSION}.tar.gz
cd R-${R_VERSION}


- Configurar e instalar R 
./configure \
    --prefix=/opt/R/${R_VERSION} \
    --enable-R-shlib \
    --enable-memory-profiling \
    --with-blas \
    --with-lapack

make
sudo make install

- Instalar Rcommander desde la pagina o CRAN MIRROR instalador de paquetes (opcionalmente puede instalarlo desde un instalador de paquetes con interfaz grafica, como
lo pueden ser : synaptic, apper....)
- En la consola desplegable y antes de la primera ejecucion digite lo siguiente y presione enter
library(Rcmdr)

Permita que instale todos los paquetes y en la primera ejecucion verifique (graficamente se ve ya la interfaz) la pestaña de >herramientas >> Cargar paquetes 
se encuentren al menos los siguientes 

- ggplot2
- nnet

Proceda a abrir el archivo utilizando el menu abrir << archivo de instruccciones y ejecute por lineas (tal y como sucede en Rstudio)

## Sugerencias ##

- Si desea subir el dataframe sugerido (Datos_temperatura_climatizacion no normalizados), puede realizarlo desde el menu Datos >> importar datos; o si por el contrario desea crear su propio archivo .csv, recuerde que hay diversas plataformas en Office por ejemplo puede crear tablas de datos e importarlas con el conjunto separación correspondiente (comas, puntos, espacios...)
- En caso de no disponer de una idea de como distribuir, o la cantidad de datos a utilizar puede cargar paquetes, y desde alli importar los dataframes disponibles (preinstalados, MASS por ejemplo) y asi explorar la herramienta mas a fondo!!
- En ocasiones e incluso en las mismas iteraciones los calculos iran a infinito o la herramienta "se saldra" esporadicamente, corregir los datos que generen vacios en
la red o asignar mas cupo para la ejecucion del aplicativo, puede ayudar a que sea menos frecuente

Recuerde que las posibilidades o tareas que se pueden realizar con este ejemplo basico incluyen:

__Validacion cruzada:__ Para evaluar la precisión y estabilidad del modelo se puede realizar la validación cruzada. Esto implica dividir datos en conjuntos de entrenamiento - validación y luego repetir el proceso de entrenamiento y validación con diferentes combinaciones de datos

__Optimización de hiperparametros:__ Investigar y ajustar los hiperparametros del modelo, como tamaño de la red, funcion de perdida, algoritmo de optimizacion etc; con el fin de mejorar el rendimiento

__Comparación de modelos:__ Como por ejemplo la regresión lineal, arbol de decisión con otras arquitecturas como la red neuronal

__Predicción de intervalos de confianza:__ Cuantificar la incertidumbre asociada a las predicciones del modelo  


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

English 

# R-Rcommander Alternative #

## Summary ##

Refrigeration technologies are generally divided into air conditioning and refrigeration applications. Air conditioning technologies are defined as those used to maintain acceptable thermal comfort conditions for people and equipment in residential, commercial and industrial buildings and spaces. , typically in an environment that is between 20° and 30°.

This alternative explores R-Rcommander where **Climatizacion55NN.R** generates the results (folder in the directory), creating a neural network and a prediction based on the normalized input data (**Datos_temperatura_climatizacion.csv**), shows how the "heat" varies as a function of a given temperature, showing it in a graph along with the prediction in the corresponding iteration (desired, see Results/Tabla_de_resultados.md)

For its part, the file **Modelo_simple_arbol.R**, which, unlike the neural network, does not need to normalize the data, the proposed dataframe is "loaded" into the directory (n = 6 observations). However, it reveals initially discouraging results, but conceptually interesting, due to the ability to segment and classify the data even with a not very good prediction. Among the alternative solutions are:

1. Check the data set for erroneous readings, gaps per iteration, among others.
2. Review and clean the data history or any reference to preprocessing (if any)
3. Analyze and reunderstand the tree model
4. The data set is so small that it does not have significant variability
5. Try to improve the tree model, for example by adjusting the tree's growth parameters; trying different modeling approaches or considering other types of statistical models that may be more suitable for this data set

Then it is important to keep in mind that the analysis and interpretation of the models can be complex, and require several iterations; It is precisely the test that is carried out in **Modelo_simple_arbolexp** increasing the amount of data in order to obtain more precise and useful results.

Finally, using the file **Guia R clustering Climatizacion**, a set of instructions **Clustering_climatizacion.R** was created with an auxiliary dataframe, to make the vector predictions, once the .csv file was imported (in this directory) it is grouping was carried out based on the centers and calculation of distances. Afterwards, with the membership vector it is possible to graph and print the prediction vector in the console. The latter was obtained using the graphical assistant of the linear regression tool (see the Results directory).

## Requirements and development platform ##

Tested and developed on Linux (Debian)

- Install dependencies

sudo sed -i.bak "/^#.deb-src.*universe$/s/^# //g" /etc/apt/sources.list
sudo apt update
sudo apt build-dep r-base

- For version 4

curl -O https://cran.rstudio.com/src/base/R-4/R-${R_VERSION}.tar.gz
tar -xzvf R-${R_VERSION}.tar.gz
cd R-${R_VERSION}


- Configure and install R
./configure \
     --prefix=/opt/R/${R_VERSION} \
     --enable-R-shlib \
     --enable-memory-profiling \
     --with-blas \
     --with-lapack

make
sudo make install

- Install Rcommander from the page or CRAN MIRROR package installer (optionally you can install it from a package installer with a graphical interface, such as: synaptic, apper...)
- In the drop-down console and before the first execution, type the following and press enter library(Rcmdr)

Allow it to install all the packages and on the first run verify (graphically you can already see the interface) the > tools tab >> Load packages that at least the following are found

- ggplot2
- nnet

Proceed to open the file using the menu open << instruction file and execute by lines (just as it happens in Rstudio)

## Suggestions ##

- If you want to upload the suggested dataframe (non-normalized Datos_temperatura_climatizacion), you can do so from the Data menu >> import data; or if, on the other hand, you want to create your own .csv file, remember that there are various platforms in Office, for example, you can create data tables and import them with the corresponding separation set (commas, points, spaces...)
- If you do not have an idea of how to distribute, or the amount of data to use, you can load packages, and from there import the available dataframes (pre-installed, MASS for example) and thus explore the tool in more depth!!
- Sometimes and even in the same iterations the calculations will go to infinity or the tool will "exit" sporadically, correcting the data that generate gaps in the network or assigning more space for the execution of the application can help make it less frequent

Remember that the possibilities or tasks that can be performed with this basic example include:

__Cross validation:__ To evaluate the accuracy and stability of the model, cross validation can be performed. This involves splitting data into training-validation sets and then repeating the training and validation process with different combinations of data.

__Hyperparameter optimization:__ Investigate and adjust the hyperparameters of the model, such as network size, loss function, optimization algorithm, etc.; in order to improve performance

__Comparison of models:__ Such as linear regression, decision tree with other architectures such as the neural network

__Prediction confidence intervals:__ Quantify the uncertainty associated with model predictions





