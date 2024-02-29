
RegModel.10 <- lm(calor~temperatura, data=Dataset)
summary(RegModel.10)

# Crear un nuevo dataframe con los valores de 'temperatura' para los que quieres predecir 'calor'
nuevos_datos <- data.frame(temperatura = c(26, 27, 28))

# Usar la función 'predict' para hacer las predicciones
predicciones <- predict(RegModel.8, nuevos_datos)

# Imprimir las predicciones
print(predicciones)


scatterplot(calor~temperatura, regLine=FALSE, smooth=FALSE, boxplots=FALSE, data=Dataset)
with(Dataset, Hist(temperatura, scale="frequency", breaks="Sturges", col="darkgray"))
library(aplpack, pos=15)
with(Dataset, stem.leaf(calor, na.rm=TRUE))
scatterplot(calor~temperatura, regLine=FALSE, smooth=FALSE, boxplots=FALSE, data=Dataset)


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

# Vector de pertenencia a clusters vistos por consola primero OJO 
clusters <- c(1, 1, 1, 2, 2, 2)

# Gráfico negro y rojo para la pertenencia de los cluster es decir: 
# Cluster means: Son los centros de los clusters. En tu caso, el primer cluster tiene un promedio de temperatura de 27 y un promedio de calor de 35. 
# El segundo cluster tiene un promedio de temperatura de 30 y un promedio de calor de 21.67.
# Clustering vector: Indica a qué cluster pertenece cada observación. En tu caso, las primeras tres observaciones pertenecen al primer cluster y las últimas tres al segundo cluster.
# Within cluster sum of squares by cluster: Es la suma de las distancias al cuadrado de cada punto a su centroide. Cuanto menor sea este valor, más “compacto” es el cluster.
#(between_SS / total_SS = 79.9 %): Esta es una medida de cuánta variación se explica por los clusters. En tu caso, el 79.9% de la variación en tus datos se explica por la pertenencia
#a los clusters.

plot(Dataset$temperatura, Dataset$calor, col = clusters)




