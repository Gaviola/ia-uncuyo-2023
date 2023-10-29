7) Validación cruzada

Funcion para realizar los pliegues:

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

Funcion para realizar la validacion cruzada:

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
        model <- rpart(inclinacion_peligrosa ~ especie + circ_tronco_cm + altura, data = train_data)
    
        # Realizar predicciones en el conjunto de prueba
        predictions <- predict(model, test_data, type = "class")
    
        # Calcular métricas para el fold actual
        confusion_matrix <- calculate_confusion_matrix(predictions, test_data$inclinacion_peligrosa)
    
        accuracies[i] <- accuracy(confusion_matrix)
        precisions[i] <- precision(confusion_matrix)
        sensitivities[i] <- sensitivity(confusion_matrix)
        specificities[i] <- specificity(confusion_matrix)
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

Teniendo en cuenta que se realizo un modelo de arbol de decision basandose en circ_tronco_cm + altura + lat + long los 
resultados entregados utilizando la validacion cruzada con 10 pliegues son los siguientes:

- Media Accuracy:  0.8883275

- Media Precision: NaN

- Media Sensitivity: 0

- MediaSpecificity: 1
 
- Desviacion Accuracy: 0.005384772

- Desviacion Precision: NaN

- Desviacion Sensitivity: 0

- Desviacion Specificity: 0

Estos resultados se deben a que el modelo recibe como datos de entrenamiento mcuho arboles sin inclinacion peligrosa, 
sumado a que los arboles de decision no son un modelo muy potente para la prediccion, desenboca en que predice todos los
casos como inclinacion no peligrosa. Esto provoca que dentro de la matriz de confusion no se encuentren falsos positivos
ni verdaderos positivos, lo que se ve plasmado en la precision o la sensibilidad.