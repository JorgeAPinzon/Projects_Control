
Dataset <- 
  read.table("su ruta de descarga/Projects_Control/Climatizacion inteligente/Alternativa R/Datos_temperatura_climatizacion.csv",
   header=TRUE, sep=",", na.strings="NA", dec=".", strip.white=TRUE)

library(rpart, pos=15)

# Ajustar el modelo de árbol de decision 
modelo_arbol <- rpart(calor ~ temperatura, data = Dataset)

# imprimir el modelo de árbol de decision 
print(modelo_arbol)

# Predecir el calor para una temperatura de 26
prediccion <- predict(modelo_arbol, newdata = data.frame(temperatura = 26))
print(prediccion)


