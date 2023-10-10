1. Describir en detalle una formulación CSP para el Sudoku.

Para resolver el sudoku, se puede utilizar un CSP descripto de la siguiente manera:

* Conjunto de variables X: { (x_i, x_j) | x, j <= 9 y x,j > 0} (cada celda del sudoku)

* Conjunto de restricciones C: {Xi != Xj | di ∈ Di != dj ∈ Dj} para cada par de variables i,j 
que se encuentren en la misma fila, columna o cuadrante.

* Conjunto de dominios Di: {1,2,3,4,5,6,7,8,9} para cada variable i

---

2. Utilizar el algoritmo AC-3 para demostrar que el arco consistencia puede detectar la
inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el
mapa de Australia (Figura 5.1 AIMA 2da edición ).

Algortimo AC-3:

```
function AC-3(csp) returns false if an inconsistency is found and true otherwise
    inputs: csp, a binary CSP with components (X, D, C)
    local variables: queue, a queue of arcs, initially all the arcs in csp
    while queue is not empty do
        (Xi, Xj )← REMOVE-FIRST(queue)
        if REVISE(csp, Xi, Xj ) then
            if size of Di = 0 then return false
            for each Xk in Xi.NEIGHBORS - {Xj} do
                add (Xk, Xi) to queue
       return true
       
function REVISE(csp, Xi, Xj ) returns true iff we revise the domain of Xi
    revised ← false
    for each x in Di do
        if no value y in Dj allows (x ,y) to satisfy the constraint between Xi and Xj then
            delete x from Di
            revised ← true
    return revised
```

Teniendo:

![](C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\Australia.png)

- X: {WA, NT, SA, Q, NSW, V, T}
- C: {Xi != Xj | di ∈ Di != dj ∈ Dj} Para todo estado adyacente entre si
- D: {rojo, verde, azul}, excepto los estados WA y V, con valor WA: {rojo} y V: {azul}

Comenzamos poniendo en una cola Q a todos los arcos,

Q: {(SA,WA), (SA,NT), (SA,Q), (SA,NSW), (SA,V), (NT,WA), (Q,NSW), (NSW,V) ...}

Luego, comenzamos a iterar sobre la cola Q, Dado que el orden en la cola no importa, podemos manejarlo 
como un conjunto y utilizar cualquier arco dentro de Q y verificar si el arco es consistente. En caso 
de serlo, no se hace nada. En caso contrario, se remueve el valor inconsistente del dominio de la variable 
Xi y se agregan a la cola Q todos los arcos (Xk, Xi) para cada variable Xk que sea adyacente a Xi. Con el fin didactico
de mostrar el funcionamiento del algoritmo, se elegiran siempre los arcos mas convenientes para la demostracion, cosa 
que en la implementacion de un algoritmo no siempre seria tan factible.

Dado el resultado parcial R: {WA = Rojo, NT = {Rojo, Verde, Azul}, SA = {Rojo, Verde, Azul}, Q = {Rojo, Verde, Azul},
NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

1) Verificamos la consistencia del arco (SA,WA). Dado que WA = Rojo, SA = {Verde, Azul}} y agregamos los arcos 
    (NT, SA), (Q, SA), (NSW, SA) y (V, SA) a la cola Q.


    R: {WA = Rojo, NT = {Rojo, Verde, Azul}, SA = {Verde, Azul}, Q = {Rojo, Verde, Azul}, NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

2) Verificamos la consistencia del arco (SA, V). Dado que V = Azul, SA = Verde y agregamos los arcos (WA, SA), (NT, SA),
    (Q,SA) y (NSW, SA) a la cola Q.


    R: {WA = Rojo, NT = {Rojo, Verde, Azul}, SA = Verde, Q = {Rojo, Verde, Azul}, NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

3) Verificamos la consistencia del arco (NT, SA). Dado que SA = Verde, NT = {Rojo, Azul} y agregamos los arcos (WA, NT) y
   (Q, NT) a la cola Q.


    R: {WA = Rojo, NT = {Rojo, Azul}, SA = Verde, Q = {Rojo, Verde, Azul}, NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

4) Verificamos la consistencia del arco (NT, WA). Dado que WA = Rojo, NT = Azul y agregamos el arco (SA, WA) a la cola Q.

    
    R: {WA = Rojo, NT = Azul, SA = Verde, Q = {Rojo, Verde, Azul}, NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

5) Verificamos la consistencia del arco (Q, NT). Dado que NT = Azul, Q = {Rojo, Verde} y agregamos los arcos (SA, Q) y
   (NSW, Q) a la cola Q.


    R: {WA = Rojo, NT = Azul, SA = Verde, Q = {Rojo, Verde}, NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

6) Verificamos la consistencia del arco (Q, SA). Dado que SA = Verde, Q = Rojo y agregamos el arco (NT, Q).

    
    R: {WA = Rojo, NT = Azul, SA = Verde, Q = Rojo, NSW = {Rojo, Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

7) Verificamos la consistencia del arco (NSW, Q). Dado que Q = Rojo, NSW = {Verde, Azul} y agregamos los arco (SA, NSW) y
   (V, NSW) a la cola Q.


    R: {WA = Rojo, NT = Azul, SA = Verde, Q = Rojo, NSW = {Verde, Azul}, V = Azul, T = {Rojo, Verde, Azul}}

8) En este punto nos encontrariamos que el dominios de NSW es {Verde, Azul} mientras que sus nodos vecinos tienen dominio
   SA = Verde y V = Azul. Por lo tanto, el algoritmo llegaria a una inconsistencia y devolveria false.

---


3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado
CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables
están relacionadas por a lo sumo un camino).

Para resolver un problema CSP estructurado en arbol con n nodos o variables y siendo d el tamaño de los dominios de cada
variable, el algoritmo AC-3 tiene una complejidad temportal de O(n*d^2). Esto se debe a que podemos conseguir una
arco-consistencia en O(n) pasos y en cada uno de ellos debemos comprar hasta d valores de cada dominio. En casos donde
el problema CSP no es estructurado en forma de arbol, la complejidad temporal puede ser aun mayor.

---

4. AC-3 coloca de nuevo en la cola todo arco (Xk , Xi) cuando cualquier valor es removido
del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de 
Xi. Supongamos que por cada arco (Xk ,Xi) se puede llevar la cuenta del número de valores
restantes de Xi que sean consistentes con cada valor de Xk. Explicar como actualizar ese 
número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo
total O(n 2d 2)

En caso de poder llevar la cuenta de los valores restantes de Xi que sean consistentes con cada valor de Xk, mediante alguna
estructura de datos, entonces tendriamos una estructura de tamaño n x d (siendo n el numero de variables y d el tamaño de
los dominios de cada variable) donde se pueden realizar modificaciones en tiempo constante. Como maximo, el problema CSP 
puede tener n^2 arcos, y como maximo pueden existir d^2 posibles comparaciones entre los valores de los dominios de cada 
variable. Por lo tanto, la complejidad temporal en este caso concreto seria de O(n^2 * d^2).

---


5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p.
172 AIMA 2da edición). Para ello, demostrar:
- a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco)
implica n-consistencia (siendo n número total de variables)

Supongamos que tenemos un CSP cuyo grafo de restricciones es un árbol con "n" variables.

Establecemos la 2-consistencia, eliminando del dominio aquellos elementos que producen inconsistencias. Esto 
garantiza que las restricciones binarias entre cada par de variables sean respetadas. En un árbol, todas las variables 
están conectadas a través de una cadena única de restricciones binarias, ya que no hay ciclos. Por lo tanto, la 
2-consistencia garantiza que todas las restricciones binarias se respeten.

Para demostrar que esto implica la n-consistencia, notamos que dado que el grafo de restricciones es un árbol,
podemos continuar aplicando la 2-consistencia a lo largo de la cadena de restricciones hasta llegar a todas las
variables. Dado que no hay ciclos, eventualmente alcanzaremos todas las variables en el CSP, haciendo que el CSP sea
n-consistente.

- b. Argumentar por qué lo demostrado en a. es suficiente

Demostrar que la 2-consistencia implica la n-consistencia en un CSP de árbol es suficiente porque en un grafo de 
restricciones que es un árbol, aplicar la 2-consistencia de manera secuencial desde un extremo de la cadena de 
restricciones hasta el otro garantiza que todas las restricciones binarias y, por lo tanto, todas las restricciones 
n-arias se cumplan.

En otras palabras, si se garantiza que las restricciones binarias se respetan en todo el árbol, entonces no hay 
posibilidad de que existan conflictos en restricciones más complejas que involucren más de dos variables. Por lo tanto, 
no es necesario verificar la consistencia para restricciones de mayor aridad, ya que se deduce de manera implícita al 
garantizar la consistencia de las restricciones binarias en un grafo de restricciones de árbol.

---

6. Implementar una solución al problema de las n-reinas utilizando una formulación CSP
- a Implementar una solución utilizando backtracking
- b. Implementar una solución utilizando encadenamiento hacia adelante.
- c. En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.
- d. En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 10, 12 y 15 reinas.
- e. Realizar un gráfico de cajas para los puntos c y d.


<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Estados_Tamaño_4.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Tiempo_Tamaño_4.png"/>

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Estados_Tamaño_8.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Tiempo_Tamaño_8.png"/>

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Estados_Tamaño_10.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Tiempo_Tamaño_10.png"/>

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Estados_Tamaño_12.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Tiempo_Tamaño_12.png"/>

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Estados_Tamaño_15.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp6-csp\boxplots\Tiempo_Tamaño_15.png"/>

