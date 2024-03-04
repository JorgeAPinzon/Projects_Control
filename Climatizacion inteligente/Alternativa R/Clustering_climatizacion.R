# Crear un nuevo dataframe con los valores de 'temperatura' para los que quieres predecir 'calor'
nuevos_datos <- data.frame(temperatura = c(26, 27, 28, 29, 30, 31))

library(aplpack, pos=15)

scatterplot(calor~temperatura, regLine=FALSE, smooth=FALSE, boxplots=FALSE, data=Dataset)
with(Dataset, Hist(temperatura, scale="frequency", breaks="Sturges", col="darkgray"))
with(Dataset, stem.leaf(calor, na.rm=TRUE))

scatterplot(calor~temperatura, regLine=FALSE, smooth=FALSE, boxplots=FALSE, data=Dataset)
Dataset <- 
  read.table("/su ruta de descarga/Projects_Control/Climatizacion inteligente/Alternativa R/Datos_temperatura_climatizacion.csv",
   header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)

# Realizar el agrupamiento k-means
set.seed(123)  # Para reproducibilidad
kmeans_resultado <- kmeans(Dataset, centers = 2)

# Verificar el resultado
print(kmeans_resultado)

# Guardar los centros de cada cluster
centers_kmeans <- kmeans_resultado$centers

# Calcular las distancias entre los centros de cada cluster
distances_kmeans <- dist(centers_kmeans)

# Realizar el agrupamiento jerárquico utilizando las distancias calculadas
hc <- hclust(d = distances_kmeans, method = "ward.D2")

 # ------------------------------------------------------------------------------------------------------------------------------#
# Vector de pertenencia a clusters vistos por consola primero OJO 
clusters <- c(1, 1, 1, 2, 2, 2)


plot(Dataset$temperatura, Dataset$calor, col = clusters)

# Regmodel.3 cargado con Estadisticos<ajuste de modelos < regresion lineal variable a explicar 'calor', variable explicativa 'temperatura'

RegModel.2 <- lm(calor~temperatura, data=Dataset)
summary(RegModel.2)
RegModel.3 <- lm(calor~temperatura, data=Dataset)
summary(RegModel.3)

# Usar la función 'predict' para hacer las predicciones
predicciones <- predict(RegModel.3, nuevos_datos)

# Imprimir las predicciones del vector nuevos datos declarados al principio 
print(predicciones)

