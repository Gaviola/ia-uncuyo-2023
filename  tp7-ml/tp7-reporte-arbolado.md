## A) Preprocesamiento
Para la realizacion de las predicciones de la inclinacion peligrosa se comenzo por realizar un Undersampling para 
intentar arreglar el desbalance existente entre las clases de arboles con inclinacion peligrosa y los que no, ya que 
dentro de los datos se encuentran en amplia mayoria ejemplos de arboles que no poseen inclinacion peligrosa. El 
subconjunto generado contiene una cantidad equitativa entre ambas clases.

Posteriormente se procedio a aplicar un peso a las clases, dando un peso mayor a la clase minoritaria (poseer 
inclinacion peligrosa) para que el modelo le de mas importancia a esta clase y asi poder obtener mejores resultados.

Finalmente como ultima etapa de preprocesamiento se excluyeron como variables predictoras a "id", "ultima_modificacion" 
ya que no son importantes para describir las caracteristicas de un arbol y las variables "area_seccion" y 
"nombre_seccion" ya que dichas variables estaban fuertemente relacionadas con la variable "seccion"

## B) Resultados sobre conjuntos de validacion

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\resultados_arboleda.png"/>

## C) Resultados de Kaggle

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\resultados_kaggle.png"/>

## D) Descripcion del algoritmo

Para la creacion del modelo predictivo se hizo uso del algoritmos Random Forest, el cual fue programado en R utilizando
la libreria original "randomForest" y la libreria "dplyr" para el preprocesamiento de los datos. El algoritmo fue
configurado con los siguientes parametros:
- ntree: 700
- mtry: 6
- classwt: matriz_costo (matrix(c(0, 5, -1, 1), nrow = 2, byrow = TRUE))

Posteriormente, los resultados obtenidos con dicho modelo son asginados de la siguiente manera:
- Probalidad < 0.5: No posee inclinacion peligrosa
- Probalidad >= 0.5: Posee inclinacion peligrosa