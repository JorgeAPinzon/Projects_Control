
# Crear un dataframe con tus datos
datos <- data.frame(
  temperatura = c(.26, .27, .28, .29, .30, .31),
  calor = c(.40, .35, .30, .25, .20, .20)
)

# Crear la red neuronal con capas ocultas
modelo <- nnet(calor ~ temperatura, data = datos, size = c(2, 2))



grafico <- ggplot(datos, aes(x = temperatura, y = calor)) +
  geom_point() +
  labs(x = "Temperatura", y = "Calor") +
  ggtitle("Relación entre Temperatura y Calor")

# Mostrar el gráfico
print(grafico)
library(nnet, pos=15)
library(ggplot2, pos=16)

# Crear un nuevo data frame con la entrada
nueva_entrada <- data.frame(temperatura = .26)

# Usar el modelo para predecir la salida
prediccion <- predict(modelo, nueva_entrada)

# Imprimir la predicción
print(prediccion*100)






