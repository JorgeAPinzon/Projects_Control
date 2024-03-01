# Alternativa R-Rcommander #

## Resumen ##

Las tecnologías de refrigeración generalmente se dividen en aplicaciones de climatización (air conditioning) y refrigeración, Las tecnologías de aire acondicionado se 
definen como aquellas que se utilizan para mantener condiciones de confort térmico aceptables para personas y equipos en edificios y espacios residenciales, comerciales 
e industriales, típicamente en un entorno que esta entre 20° y 30°. 

Esta alternativa explora R-Rcommander donde **Climatizacion55NN.R** genera los resultados (carpeta en el directorio), creando una red neuronal y una predicción en base a 
los datos normalizados de entrada (**Datos_temperatura_climatizacion.csv**), muestra como varia el "calor" en funcion de una temperatura dada, mostrandolo en un grafico 
junto con la predicción en la iteración correspondiente (deseada ver Resultados/Tabla_de_resultados.md)

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

- Si desea subir el dataframe sugerido (Datos_temperatura_climatizacion no normalizados), puede realizarlo desde el menu Datos >> importar datos; o si por el contrario desea crear su propio archivo .csv, recuerde que hay diversas plataformas en Excel por ejemplo puede crear tablas de datos e importarlas con el conjunto separación correspondiente (comas, puntos, espacios...)
- En caso de no disponer de una idea de como distribuir, o la cantidad de datos a utilizar puede cargar paquetes, y desde alli importar los dataframes disponibles (preinstalados, MASS por ejemplo) y asi explorar la herramienta mas a fondo!!
- En ocasiones e incluso en las mismas iteraciones los calculos iran a infinito o la herramienta "se saldra" esporadicamente, corregir los datos que generen vacios en
la red o asignar mas cupo para la ejecucion del aplicativo puede ayudar a que sea menos frecuente

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

English 






