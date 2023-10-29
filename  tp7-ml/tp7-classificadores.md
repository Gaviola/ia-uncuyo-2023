4)
- d. A partir de la columna recientemente generada y la columna con la clase (inclinación peligrosa) calcular utilizando
lenguaje R (dplyr) el número de:
  - i. Número de árboles CON inclinación peligrosa que fueron correctamente predicho como peligrosos por el 
  modelo/algoritmo. (True Positive)
  - ii. Número de árboles SIN inclinación peligrosa que fueron correctamente predicho como no peligrosos por el modelo.
  (True Negative)
  - iii. Número de árboles SIN inclinación peligrosa que fueron incorrectamente predicho como peligrosos según el modelo.
  (False Positives)
  - iv. Número de árboles CON inclinación peligrosa que fueron incorrectamente predicho como no peligrosos según el 
  modelo. (False Negatives)

| n = 25530     | Positivo Predecido | Negativo Predecido |
|---------------|--------------------|--------------------|
| Positivo Real | 1419               | 1432               |
| Negativo Real | 11403              | 11276              |

5) Clasificador por clase mayoritaria:
- a. Implementar una función de nombre biggerclass_classifier, que reciba como parámetro el dataframe generado con 
anterioridad y genere una nueva columna de nombre prediction_class en donde se asigne siempre de la clase mayoritaria
La función deberá devolver el dataframe original junto a la nueva columna generada.
- b. Repetir los puntos 4.c y 4.d pero aplicando la nueva función
biggerclass_classifier

La clase mayoritaria elegida fueron los arboles sin inclinacion peligrosa.

| n = 25530      | Positivo Predecido | Negativo Predecido |
|----------------|--------------------|--------------------|
| Positivo Real  | 0                  | 2851               |
| Negativo Real  | 0                  | 22679              |

6) A partir de una matriz de confusión es posible calcular distintas métricas que nos permiten determinar la calidad del
modelo de clasificación. Utilizar la siguiente imagen como guía crear funciones para calcular: Accuracy, Precision, 
Sensitivity, Specificity y calcularlas para las matrices de confusión generadas en los puntos 4 y 5
  - Random Prediction
    - Accuracy: 0.4972581
    - Precision: 0.1106692
    - Sensitivity: 0.4977201
    - Specificity: 0.4972001 
  

  - Bigger Class
    - Accuracy: 0.8883275
    - Precision: 0
    - Sensitivity: 0
    - Specificity: 1



