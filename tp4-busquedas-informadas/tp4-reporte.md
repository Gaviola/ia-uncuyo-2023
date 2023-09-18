B) Ejecutar un total de 30 veces el algoritmo A* en un escenario aleatorio
con una tasa de obstáculos del 8 por ciento, calcular la media y la
desviación estándar de la cantidad de estados explorados para llegar al
destino (si es que fue posible). Evaluar cada uno de los algoritmos sobre el
mismo conjunto de datos generado. Presentar los resultados en un gráfico
de cajas y bigotes o boxplots. Incluya también los resultados obtenidos en
el punto B del TP3 sobre búsquedas no informadas.

![](C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp4-busquedas-informadas\result_boxplot.png)

***BFS:***

- **μ**: 3673.9333333333334 Nodos Explorados
- **σ**: 2408.015736764556 Desviación Estándar de Nodos Explorados

***DFS:***

- **μ**: 8465.033333333333 Nodos Explorados
- **σ**: 5696.568994508484 Desviación Estándar de Nodos Explorados

***DFS Limitado (limitado a 1000 nodos de profundidad):***

- **μ**: 4096.4 Nodos Explorados
- **σ**: 4489.622928641035 Desviación Estándar de Nodos Explorados

***UCS:***

- **μ**: 3673.9333333333334 Nodos Explorados
- **σ**: 2408.015736764556 Desviación Estándar de Nodos Explorados

***A*:***

- **μ**: 799.8666666666667 Nodos Explorados
- **σ**: 732.0937255491989 Desviación Estándar de Nodos Explorados

La heuristica implementada para el algoritmo A* es la distancia de manhattan entre el nodo actual y el nodo destino.