library(randomForest)
library(dplyr)

#cargo los datos
data <- read.csv("Data/arbolado-mza-dataset.csv")
data_test <- read.csv("Data/arbolado-mza-dataset-test.csv")

# Filtrar todos los arboles con inclinacion peligrosa
muestra_inclinacion_peligrosa <- data[data$inclinacion_peligrosa == 1, ]

# Filtrar algunos arboles con inclinacion no peligrosa (la misma cantidad que exita de inclinacion peligrosa para balancear)
muestra_inclinacion_no_peligrosa <- data %>% filter(inclinacion_peligrosa == 0) %>% sample_n(3500)

# Unir los dos conjuntos de datos
data_filtrado <- rbind(muestra_inclinacion_peligrosa, muestra_inclinacion_no_peligrosa)

#Aplicamos un peso a las clases para balancear el dataset
matriz_costo <- matrix(c(0, 5, -1, 1), nrow = 2, byrow = TRUE)

#transformar variables categoricas a numericas (Funciona mejor si no transformas las variables categoricas)
#data_filtrado$altura <- as.integer(factor(data_filtrado$altura))
#data_filtrado$diametro_tronco <- as.integer(factor(data_filtrado$diametro_tronco))

#Establecer predictores y respuesta para randomforest
predictores <- data_filtrado[, colnames(data_filtrado) != "inclinacion_peligrosa" & colnames(data_filtrado) != "id" & colnames(data_filtrado) != "nombre_seccion" & colnames(data_filtrado) != "area_seccion" & colnames(data_filtrado) != "ultima_modificacion"]
respuesta <- data_filtrado$inclinacion_peligrosa

# Entrenamiento del modelo Random Forest
modelo <- randomForest(x = predictores, y = respuesta, ntree = 700, mtry = 6, classwt = matriz_costo)

predictions <- predict(modelo, newdata = data_test)

predicciones_transformadas <- ifelse(predictions >= 0.5, 1, 0)

print(modelo)

resultado <- data.frame(data_test$id, predicciones_transformadas)

resultado <- resultado %>% rename("ID" = "data_test.id")

resultado <- resultado %>% rename("inclinacion_peligrosa" = "predicciones_transformadas")

head(resultado)

# Utiliza write.csv2() para guardar el dataframe en un archivo CSV con punto y coma como delimitador
write.csv(resultado, file = "resultados.csv", row.names = FALSE,)