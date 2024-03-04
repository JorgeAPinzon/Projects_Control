
datos <- data.frame(
  temperatura = c(26, 27, 28, 29, 30, 31,27, 28, 29, 30, 31,27, 28, 29, 30, 31,27, 28, 29, 30, 31,27, 28, 29, 30, 31,27, 28, 29, 30, 31),
  calor = c(40, 35, 30, 25, 20, 20,35, 30, 25, 20, 20,35, 30, 25, 20, 20,35, 30, 25, 20, 20,35, 30, 25, 20, 20,35, 30, 25, 20, 20)
)
library(rpart, pos=15)

# Ajustar el modelo de árbol de decision 
modelo_arbol <- rpart(calor ~ temperatura, data = datos)

# imprimir el modelo de árbol de decision 
print(modelo_arbol)

# Predecir el calor para una temperatura de 26
prediccion <- predict(modelo_arbol, newdata = data.frame(temperatura = 26))
print(prediccion)


