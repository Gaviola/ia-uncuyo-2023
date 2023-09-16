**B) Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio
con una tasa de obstáculos del 8 por ciento, calcular la media y la
desviación estándar de la cantidad de estados explorados para llegar al
destino (si es que fue posible). Evaluar cada uno de los algoritmos sobre el
mismo conjunto de datos generado. Presentar los resultados en un gráfico
de cajas y bigotes o boxplots.**

![Boxplot](C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp3-busquedas-no-informadas\boxplot_busqueda_no_informada.png)

***BFS:***

- **μ**: 5181.266666666666 Nodos Explorados
- **σ**:2723.6666834065527 Desviación Estándar de Nodos Explorados

***DFS:***

- **μ**:5291.4 Nodos Explorados
- **σ**: 2938.4264801608265 Desviación Estándar de Nodos Explorados

***DFS Limitado (Se utilizo un limite de 1000 nodos de profundidad):***

- **μ**: 6336.4 Nodos Explorados
- **σ**: 3313.456624131362 Desviación Estándar de Nodos Explorados

***UCS:***

- **μ**: 9445.166666666666 Nodos Explorados
- **σ**:  4991.032199809998 Desviación Estándar de Nodos Explorados

---
**C) Cuál de los 3 algoritmos considera más adecuado para resolver el
problema planteado en A)?. Justificar la respuesta.**

Dados los resultados planteados en el punto B), se puede observar que el algoritmo mas adecuado
para resolver el problema es el algoritmo **BFS**. Esto es debido a que fue el algoritmo con una
mejor performance en cuanto a la cantidad de nodos explorados, ademas de que dicho algoritmo nos garantiza
encontrar el camino mas corto entre el nodo inicial y el nodo destino, cosa que no nos garantizaria
el algoritmo **DFS**.