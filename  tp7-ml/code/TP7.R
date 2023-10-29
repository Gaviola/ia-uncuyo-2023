library(ggplot2)
library(dplyr)
library(rpart)


# Cargar tu conjunto de datos
datos <- read.csv(" tp7-ml/data/arbolado-mza-dataset.csv/arbolado-mza-dataset.csv")

# Definir el tamaño de la muestra de validación (20%)
tamano_muestra_validacion <- 0.20 * nrow(datos)

# Crear un vector de índices aleatorios
indices_aleatorios <- sample(1:nrow(datos), tamano_muestra_validacion)

# Seleccionar las filas correspondientes a la muestra de validación
datos_validacion <- datos[indices_aleatorios, ]

# Seleccionar las filas restantes para el conjunto de entrenamiento
datos_entrenamiento <- datos[-indices_aleatorios, ]

# Guardar los conjuntos en archivos CSV
write.csv(datos_validacion, file = "../data/arbolado-mendoza-dataset-validation.csv", row.names = FALSE)
write.csv(datos_entrenamiento, file = "../data/arbolado-mendoza-dataset-train.csv", row.names = FALSE)

#---------------------------------------------------------------
#2)
#a)
# Calcular la distribución de la clase "inclinacion_peligrosa"
distribucion_clase <- table(datos_entrenamiento$inclinacion_peligrosa)

distribucion <- data.frame(Clase = names(distribucion_clase), Frecuencia = as.numeric(distribucion_clase))

# Crear un gráfico de barras
ggplot(distribucion, aes(x = Clase, y = Frecuencia)) +
  geom_bar(stat = "identity") +
  labs(title = "Distribucion de la Clase Inclinacion Peligrosa", x = "Clase", y = "Frecuencia")

#b)

# Calcular la frecuencia de inclinación peligrosa por sección
secciones_peligrosas <- aggregate(inclinacion_peligrosa ~ seccion, data = datos_entrenamiento, FUN = function(x) sum(x == 1))

# Ordenar el resumen en orden descendente
secciones_peligrosas_ordenada <- secciones_peligrosas[order(-secciones_peligrosas$inclinacion_peligrosa), ]

# Sección más peligrosa
seccion_mas_peligrosa <- secciones_peligrosas_ordenada[1, ]

# Crear un gráfico de barras
ggplot(secciones_peligrosas_ordenada, aes(x = seccion, y = inclinacion_peligrosa)) +
  geom_bar(stat = "identity") +
  labs(title = "Peligrosidad de las Secciones", x = "Seccion", y = "Frecuencia de Inclinacion Peligrosa")

#c)

# Calcular la frecuencia de inclinación peligrosa por especie
especies_peligrosas <- aggregate(inclinacion_peligrosa ~ especie, data = datos_entrenamiento, FUN = function(x) sum(x == 1))

# Ordenar el resumen en orden descendente
especies_peligrosas_ordenado <- especies_peligrosas[order(-especies_peligrosas$inclinacion_peligrosa), ]

# Crear un gráfico de barras
ggplot(especies_peligrosas_ordenado, aes(x = reorder(especie, -inclinacion_peligrosa), y = inclinacion_peligrosa)) +
  geom_bar(stat = "identity") +
  labs(title = "Peligrosidad de las Especies", x = "Especie", y = "Frecuencia de Inclinacion Peligrosa") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Calcular la distribución de la clase "especie"
distribucion_especie <- table(datos_entrenamiento$especie)

especies <- data.frame(Clase = names(distribucion_especie), Frecuencia = as.numeric(distribucion_especie))

# Crear un gráfico de barras
ggplot(especies, aes(x = Clase, y = Frecuencia)) +
  geom_bar(stat = "identity") +
  labs(title = "Distribucion de la Clase Inclinacion Peligrosa", x = "Clase", y = "Frecuencia")

# Crear un dataframe con las especies y la cantidad de árboles con inclinación peligrosa
peligrosidad_por_especie <- data.frame(
  Especie = names(especies),
  Arboles_Con_Inclinacion_Peligrosa = rep(0, length(especies))
)

especies_por_peligrosidad <- datos_entrenamiento %>%
  group_by(especie) %>%
  summarize(proporcion_peligrosa = mean(inclinacion_peligrosa)) %>%
  arrange(desc(proporcion_peligrosa))

# Crear un gráfico de barras
ggplot(especies_por_peligrosidad, aes(x = especie, y = proporcion_peligrosa)) +
  geom_bar(stat = "identity") +
  labs(title = "Distribucion de especie en base a la inclinacion peligrosa", x = "Clase", y = "Frecuencia")

# Calcular la cantidad de algarrobos en el dataset
algarrobos <- sum(datos_entrenamiento$especie == "Algarrobo")

#--------------------------------------------------------------------------
#3)
#a)
# Definir el número de bins que se desea probar
num_bins <- c(10, 20, 30, 40)

# Crear un espacio para el gráfico de múltiples histogramas
par(mfrow=c(2, 2)) # 2 filas y 2 columnas de gráficos

# Generar histogramas para diferentes números de bins
for (i in num_bins) {
  hist(datos_entrenamiento$circ_tronco_cm, main = paste("Numero de bins =", i),
       xlab = "Circunferencia del tronco (cm)", col = "lightblue", breaks = i)
}

#b)
# Crear un histograma separando por el atributo inclinacion_peligrosa
par(mfrow=c(1, 2)) # Organizar los histogramas en una fila con dos columnas

# Histograma para inclinacion_peligrosa = 0
hist(datos_entrenamiento$circ_tronco_cm[datos_entrenamiento$inclinacion_peligrosa == 0],
     main = "Inclinacion no peligrosa",
     xlab = "Circunferencia del tronco (cm)",
     col = "blue",
     breaks = 20)

# Histograma para inclinacion_peligrosa = 1
hist(datos_entrenamiento$circ_tronco_cm[datos_entrenamiento$inclinacion_peligrosa == 1],
     main = "Inclinacion peligrosa",
     xlab = "Circunferencia del tronco (cm)",
     col = "red",
     breaks = 20)

# Restaurar la configuración por defecto
par(mfrow=c(1, 1))

#c)

# Definir los puntos de corte para cada categoría
cortes <- quantile(datos_entrenamiento$circ_tronco_cm, probs = c(0, 0.25, 0.5, 0.75, 1))
valores <- c("bajo", "medio", "alto", "muyalto")

# Crear la nueva variable categórica circ_tronco_cm_cat
datos_entrenamiento$circ_tronco_cm_cat <- cut(datos_entrenamiento$circ_tronco_cm, breaks = cortes, labels = valores, include.lowest = TRUE)

# Guardar el nuevo dataframe en un archivo CSV
write.csv(datos_entrenamiento, file = "arbolado-mendoza-dataset-circ_tronco_cm-train.csv", row.names = FALSE)

#--------------------------------------------------------------------------
#4)

#a)
agregar_columna_aleatoria <- function(data) {
  # Generar valores aleatorios entre 0 y 1
  valores_random <- runif(nrow(data), min = 0, max = 1)

  # Agregar la nueva columna al data.frame
  data$prediction_prob <- valores_random

  # Devolver el data.frame con la nueva columna
  return(data)
}

#b)
# Función para generar la columna prediction_class
random_classifier <- function(data) {
  # Aplicar el criterio y generar la nueva columna
  data$prediction_class <- ifelse(data$prediction_prob > 0.5, 1, 0)

  # Devolver el data.frame con la nueva columna
  return(data)
}

#c)

arbolado_random <- agregar_columna_aleatoria(datos_entrenamiento)
arbolado_random <- random_classifier(arbolado_random)

#d)

#contar cantidad de casos
total_cases <- nrow(arbolado_random)

# Calcular la matriz de confusión utilizando dplyr
matriz_de_confusion <- arbolado_random %>%
  mutate(True_Positive = ifelse(prediction_class == 1 & inclinacion_peligrosa == 1, 1, 0),
         True_Negative = ifelse(prediction_class == 0 & inclinacion_peligrosa == 0, 1, 0),
         False_Positive = ifelse(prediction_class == 1 & inclinacion_peligrosa == 0, 1, 0),
         False_Negative = ifelse(prediction_class == 0 & inclinacion_peligrosa == 1, 1, 0)) %>%
  summarise(
    True_Positive = sum(True_Positive),
    True_Negative = sum(True_Negative),
    False_Positive = sum(False_Positive),
    False_Negative = sum(False_Negative)
  )

# Imprimir la matriz
cat("Verdaderos Positivos: ", matriz_de_confusion$True_Positive, "\n")
cat("Verdaderos Negativos: ", matriz_de_confusion$True_Negative, "\n")
cat("Falsos Positivos: ", matriz_de_confusion$False_Positive, "\n")
cat("Falsos Negativos: ", matriz_de_confusion$False_Negative, "\n")
cat("Cantidad de casos: ", total_cases, "\n")

#--------------------------------------------------------------------------

# Definir la función biggerclass_classifier
biggerclass_classifier <- function(data) {
  # Calcular la clase mayoritaria
  majority_class <- as.numeric(names(sort(table(data$inclinacion_peligrosa), decreasing = TRUE)[1]))

  # Crear la nueva columna prediction_class con la clase mayoritaria
  data$prediction_class <- majority_class

  # Devolver el dataframe con la nueva columna
  return(data)
}

arbolado_clase_mayor <- agregar_columna_aleatoria(datos_entrenamiento)
arbolado_clase_mayor <- biggerclass_classifier(arbolado_random)

total_cases2 <- nrow(arbolado_clase_mayor)

matriz_de_confusion2 <- arbolado_clase_mayor %>%
  mutate(True_Positive = ifelse(prediction_class == 1 & inclinacion_peligrosa == 1, 1, 0),
         True_Negative = ifelse(prediction_class == 0 & inclinacion_peligrosa == 0, 1, 0),
         False_Positive = ifelse(prediction_class == 1 & inclinacion_peligrosa == 0, 1, 0),
         False_Negative = ifelse(prediction_class == 0 & inclinacion_peligrosa == 1, 1, 0)) %>%
  summarise(
    True_Positive = sum(True_Positive),
    True_Negative = sum(True_Negative),
    False_Positive = sum(False_Positive),
    False_Negative = sum(False_Negative)
  )

# Imprimir la matriz
cat("Verdaderos Positivos: ", matriz_de_confusion2$True_Positive, "\n")
cat("Verdaderos Negativos: ", matriz_de_confusion2$True_Negative, "\n")
cat("Falsos Positivos: ", matriz_de_confusion2$False_Positive, "\n")
cat("Falsos Negativos: ", matriz_de_confusion2$False_Negative, "\n")
cat("Cantidad de casos: ", total_cases2, "\n")

#--------------------------------------------------------------------------

accuracy <- function(confusion_matrix) {
  TP <- confusion_matrix$True_Positive
  TN <- confusion_matrix$True_Negative
  FP <- confusion_matrix$False_Positive
  FN <- confusion_matrix$False_Negative
  return((TP + TN) / (TP + TN + FP + FN))
}

precision <- function(confusion_matrix) {
  TP <- confusion_matrix$True_Positive
  FP <- confusion_matrix$False_Positive
  return(TP / (TP + FP))
}

sensitivity <- function(confusion_matrix) {
  TP <- confusion_matrix$True_Positive
  FN <- confusion_matrix$False_Negative
  return(TP / (TP + FN))
}

specificity <- function(confusion_matrix) {
  TN <- confusion_matrix$True_Negative
  FP <- confusion_matrix$False_Positive
  return(TN / (TN + FP))
}

acc_random <- accuracy(matriz_de_confusion)
pre_random <- precision(matriz_de_confusion)
sen_random <- sensitivity(matriz_de_confusion)
spe_random <- specificity(matriz_de_confusion)

acc_mayor <- accuracy(matriz_de_confusion2)
pre_mayor <- precision(matriz_de_confusion2)
sen_mayor <- sensitivity(matriz_de_confusion2)
spe_mayor <- specificity(matriz_de_confusion2)

cat("Acurracy Random: ", acc_random, "\n")
cat("Precision Random: ", pre_random, "\n")
cat("Sensitivity Random: ", sen_random, "\n")
cat("Specificity Random: ", spe_random, "\n")

cat("Acurracy Mayor: ", acc_mayor, "\n")
cat("Precision Mayor: ", pre_mayor, "\n")
cat("Sensitivity Mayor: ", sen_mayor, "\n")
cat("Specificity Mayor: ", spe_mayor, "\n")

#--------------------------------------------------------------------------
#7)

create_folds <- function(data, num_folds) {
  # Obtener el número total de filas en el dataframe
  total_rows <- nrow(data)

  # Crear una secuencia de índices del dataframe
  indices <- 1:total_rows

  # Mezclar los índices aleatoriamente
  shuffled_indices <- sample(indices)

  # Dividir los índices en folds
  folds <- split(shuffled_indices, 1:num_folds)

  # Devolver la lista de folds
  return(folds)
}

cross_validation <- function(data, num_folds) {
  # Crear folds
  folds <- create_folds(data, num_folds)

  # Inicializar vectores para almacenar las métricas de cada fold
  accuracies <- vector("numeric", length = num_folds)
  precisions <- vector("numeric", length = num_folds)
  sensitivities <- vector("numeric", length = num_folds)
  specificities <- vector("numeric", length = num_folds)

  for (i in 1:num_folds) {
    # Separar el dataframe en entrenamiento y prueba según el fold actual
    test_indices <- folds[[i]]
    train_indices <- unlist(folds[-i])
    train_data <- data[train_indices, ]
    test_data <- data[test_indices, ]

    # Entrenar un modelo de árbol de decisión con rpart
    model <- rpart(inclinacion_peligrosa ~ circ_tronco_cm + altura + lat + long , data = train_data, method = "class")

    # Realizar predicciones en el conjunto de prueba
    predictions <- predict(model, test_data, type = "class")

    # Calcular métricas para el fold actual
   matriz_de_confusion <- data.frame(
  True_Positive = sum(predictions == 1 & test_data$inclinacion_peligrosa == 1),
  True_Negative = sum(predictions == 0 & test_data$inclinacion_peligrosa == 0),
  False_Positive = sum(predictions == 1 & test_data$inclinacion_peligrosa == 0),
  False_Negative = sum(predictions == 0 & test_data$inclinacion_peligrosa == 1)
)

    accuracies[i] <- accuracy(matriz_de_confusion)
    precisions[i] <- precision(matriz_de_confusion)
    sensitivities[i] <- sensitivity(matriz_de_confusion)
    specificities[i] <- specificity(matriz_de_confusion)
  }

  # Calcular la media y desviación estándar de las métricas
  mean_accuracy <- mean(accuracies)
  mean_precision <- mean(precisions)
  mean_sensitivity <- mean(sensitivities)
  mean_specificity <- mean(specificities)

  sd_accuracy <- sd(accuracies)
  sd_precision <- sd(precisions)
  sd_sensitivity <- sd(sensitivities)
  sd_specificity <- sd(specificities)

  # Devolver las métricas promedio y desviación estándar
  results <- list(
    Mean_Accuracy = mean_accuracy,
    Mean_Precision = mean_precision,
    Mean_Sensitivity = mean_sensitivity,
    Mean_Specificity = mean_specificity,
    SD_Accuracy = sd_accuracy,
    SD_Precision = sd_precision,
    SD_Sensitivity = sd_sensitivity,
    SD_Specificity = sd_specificity
  )

  return(results)
}

resultados_arbol_decicion <- cross_validation(datos_entrenamiento, 10)

print(resultados_arbol_decicion)
