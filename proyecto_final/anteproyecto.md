# Predicción de resultados de partidas de LOL

## Integrantes
- Luciano Masuelli
- Facundo Gaviola

***Codigo del proyeto: LOL***

## Descripción
League of Legends (LoL) es un popular videojuego de estrategia en tiempo real que ha alcanzado una inmensa popularidad 
desde su lanzamiento en 2009. En este juego, dos equipos de cinco jugadores se enfrentan en un campo de batalla virtual, 
cada uno controlando un campeón con habilidades únicas. LoL ha dejado una marca indeleble en el mundo de los esports, 
destacándose por su enorme base de jugadores, la celebración del Campeonato Mundial anual con premios millonarios, y el 
establecimiento de ligas profesionales en diversas regiones. Además, la transmisión en plataformas como Twitch ha 
atraído a una audiencia global, contribuyendo a la profesionalización y popularidad de los deportes electrónicos.

## Objetivos
Predecir correctamente en base a los datos de una partida cuál de los dos equipos va a obtener la victoria. También se
busca determinar que factores son los que mas afectan al resultado de una partida y cuanto podria llegar a durar la 
partida dada una serie de factores iniciales.

## Dataset
Para la realizacion de este proyecto se utilizara un dataset que consiste en 100800 partidas de las categorias 
challenger, grandmaster y master de la temporada 2020 de League of Legends en la region de Corea. Dentro de este dataset
se pueden hacer uso de muchas variables, como por ejemplo:
- gameDuration: Duracion de la partida
- win: Si el equipo gano o perdio
- firstBlood: Si el equipo obtuvo la primera sangre
- firstTower: Si el equipo destruyo la primera torre
- firstDragon: Si el equipo obtuvo el primer dragon

Juntos con otros datos que pueden ser utilizados para la creacion de un modelo de machine learning.

Link:
https://www.kaggle.com/datasets/gyejr95/league-of-legendslol-ranked-games-2020-ver1/data?select=match_winner_data_version1.csv

## Alcance
Lograr predecir el resultado de una partida mediante un modelo de machine learning adecuado. Para esto se implementará 
un algoritmo de Random Forest o alguna implementacion de boosting.

## Limitaciones
- Falta de datos, ya que hay factores que influyen en el juego que no son planteados en los datos.
- El constante cambio que tiene el juego a lo largo del tiempo dificulta que un modelo pueda mantenerse en el tiempo 
funcionando de manera correcta.

## Métricas
Para la evaluacion del desempeño de los algoritmos se utilizaran las siguientes metricas:
* Cantidad de partidas predichas correctamente / Cantidad total de partidas (F-score)

Se evaluaran especificamente sensibilidad y especificidad, ya que se busca que el modelo pueda predecir correctamente ya
que se consigue un mayor valor al lograr predecir si un equipo logra la victorio o es derrotado que si se predice
incorrectamente.

## Justificación
La predicción del resultado de una partida implica considerar una amplia gama de factores y variables que resultan 
difíciles de gestionar mediante un software estocástico. Por esta razón, un modelo capaz de comprender la interacción 
entre los datos presentes en una partida y su influencia en las predicciones se presenta como una opción más conveniente 
en comparación con un programa tradicional.

## Listado de actividades a realizar
1. Recopilación de datos [1 dia]
2. Limpieza y puesta a punto del dataset [3 dias]
3. Estudio de los atributos más descriptivos [2 dias]
4. Investigación de modelos aplicables al problema [7 dias]
5. Evaluación de distintos modelos de machine learning [7 dias]
6. Comparar resultados de los distintos modelos frente a un algoritmo aleatorio [2 dias]
7. Obtención de métricas para evaluar resultados [1 dia]
8. Análisis de los resultados [1 dia]
9. Optimización del código [2 dias]

## Diagrama de Gantt
![](C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\proyecto_final\diagrama_gantt.png)


## Papers o Referencias
https://www.researchgate.net/publication/353766670_Using_Machine_Learning_to_Predict_Game_Outcomes_Based_on_Player-Champion_Experience_in_League_of_Legends
https://www.researchgate.net/publication/358824595_Machine_Learning_Methods_for_Predicting_League_of_Legends_Game_Outcome
https://link.springer.com/article/10.1007/s42979-022-01660-6
