1. For each of parts (a) through (d), indicate whether we would generally expect the performance of a flexible 
statistical learning method to be better or worse than an inflexible method. Justify your answer.


- (a) The sample size n is extremely large, and the number of predictors p is small.

Dado que se tiene un gran numero de observaciones n, es esperable que un metodo flexible logre un mejor resultado en 
comparacion a un metodo inflexible. Esto se debe a que un metodo flexible puede ajustarse mejor cuando tenemos una gran
cantidad de datos. además, al tener un gran numero de observaciones, reducimos el riesgo de overfitting y de 
alteraciones por ruido en los datos. Es importante destacar que en el caso de que se quiera hacer una interpretacion, 
un metodo inflexible puede llegar a ser una mejor opcion, debido a su simplicidad.

- (b) The number of predictors p is extremely large, and the number of observations n is small.

En este caso, un metodo inflexible puede llegar a ser una mejor opcion, debido a que teniendo un numero limitado de 
observaciones y un gran numero de predictores, un metodo flexible puede llegar a hacer ajustes demasiado finos y por lo 
tanto, overffitear los datos. Además, al tener un gran numero de predictores, un metodo inflexible puede ayudar a reducir
la complejidad del modelo. Tambien es importante destacar que al igual que en el caso anterior, siempre es mas sencillo
interpretar un modelo inflexible.


- (c) The relationship between the predictors and response is highly non-linear.

En este caso, un metodo flexible puede llegar a ser una mejor opcion, esto se debe a que un metodo flexible puede 
ajustarse mejor a un modelo no lineal. Por ejemplo, una regresion linear claramente tendria muchos problemas para
ajustarse a dicho modelo. sin embargo, un metodo flexible como un arbol de decision o random forest, puede moldearse 
correctamente a un modelo no lineal.


- (d) The variance of the error terms, i.e. σ2 = Var(ϵ), is extremely high.

En este caso, un metodo inflexible es preferible a un flexible. Dicha eleccion se puede sustentar en que un metodo 
inflexible es mas robusto frente al ruido de los datos.

2. Explain whether each scenario is a classification or regression problem, and indicate whether we are most interested 
in inference or prediction. Finally, provide n and p.


- (a) We collect a set of data on the top 500 firms in the US. For each firm we record profit, number of employees, 
industry and the CEO salary. We are interested in understanding which factors affect CEO salary.

El problema planteado es un problema de regresion. ya que queremos predecir cual seria el salario de un CEO dado un
conjunto de variables. Además, estamos interesados en la inferencia, ya que se quiere comprender que factores y en que
medida afectan al salario de un CEO. En este caso concreto tenemos, n = 500 (Informacion de las firmas) y p = 3. 
(ingresos, numero de empleados y industria), siendo la variable respuesta el salario del CEO.

- (b) We are considering launching a new product and wish to know whether it will be a success or a failure. We collect
data on 20 similar products that were previously launched. For each product we have recorded whether it was a success or
failure, price charged for the product, marketing budget, competition price, and ten other variables.

El problema planteado es un problema de clasificacion. Ya que queremos predecir si un producto sera un exito o un 
fracaso (basicamente se clasifican los productos en "exito" o "fracaso"). También, estamos interesados en predecir, ya
que queremos saber si un producto sera un exito y tomar una decision en base a eso. En este caso concreto tenemos,
n = 20 (productos) y p = 13 (precio del producto, presupuesto de marketing y otra 10 variables).

- (c) We are interested in predicting the % change in the USD/Euro exchange rate in relation to the weekly changes in
the world stock markets. Hence, we collect weekly data for all of 2012. For each week we record the % change in the 
USD/Euro, the % change in the US market, the % change in the British market, and the % change in the German market.

El problema planteado es un problema de regresion. En este se quiere predecir el porcentaje de cambio entre el USD y el
Euro en relacion a los cambios semanales de los mercados. Por lo tanto, buscamos predecir como se modificara el 
porcentaje de cambio. En el problema tenemos, n = 52 ( 1 año = 52 semanas aprox) y p = 3 (el porcentaje de cambio en 
los mercados de EEU, Inglaterra y Alemania).



5. What are the advantages and disadvantages of a very flexible (versus a less flexible) approach for regression or 
classification? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When
might a less flexible approach be preferred?

La flexibilidad de un metodo tiene que ver con la forma que tomara la funcion f que se ajustara a los datos. Las
ventajas que brinda un modelo mas flexible son:
 * Pueden adaptarse mejor a informacion compleja o cuando tenemos muchos datos y pocos predictores.
 * Puede predecir de mejor manera aquellos datos que no se comporten en forma lineal o no se conozca la forma.

Las desventajas de un modelo mas flexible son:
 * Son modelos propensos a overfittear los datos.
 * Generalmente, son modelos mas dificiles de interpretar.
 * Requieren de un mayor tiempo de computo.

Generalmente un modelo mas flexible es preferible en aquellos casos donde exista evidencia de que las relaciones entre 
los datos son complejas, tengamos muchos datos en nuestro dataset y que busquemos unicamente hacer una prediccion, es 
decir, la interpretacion no es importante para el problema. Por otro lado, un modelo menos flexible es preferible cuando 
tenemos pocos datos y muchas variables con los que trabajar, y se busque una interpretacion del modelo o se quieran 
reducir los tiempos de computo.

6. Describe the differences between a parametric and a non-parametric statistical learning approach. What are the 
advantages of a parametric approach to regression or classification (as opposed to a nonparametric approach)? What are 
its disadvantages?

El aprendizaje estadistico parametrico consiste en reducir el problema de estimar la funcion f a un numero de parametros,
asumiendo la forma de f. Por el otro lado, los modelos no parametricos no asumen una forma para f y dejan que los
parametros se ajusten en funcion de los datos.

Las ventajas de un modelo parametrico son:
 * Son mas simples de interpretar.
 * Reducen la probabilidad de overfitting.
 * Son mas faciles de computar.

Las desventajas de un modelo parametrico son:
 * Si la forma de f no se ajusta a los datos, el modelo no se ajustara correctamente.
 * Los modelos parametricos pueden no ser optimos para capturar relaciones no lineales.

7. The table below provides a training data set containing six observations, three predictors, and one qualitative 
response variable.

| Obs | X1 | X2 | X3 | Y     |
|-----|----|----|----|-------|
| 1   | 0  | 3  | 0  | Red   |
| 2   | 2  | 0  | 0  | Red   |
| 3   | 0  | 1  | 3  | Red   |
| 4   | 0  | 1  | 2  | Green |
| 5   | -1 | 0  | 1  | Green |
| 6   | 1  | 1  | 1  | Red   |

Suppose we wish to use this data set to make a prediction for Y when X1 = X2 = X3 = 0 using K-nearest neighbors.

- a) Compute the Euclidean distance between each observation and the test point, X1 = X2 = X3 = 0.

| Obs | Distancia Euclideana               |
|-----|------------------------------------|
| 1   | sqrt(0^2 + 3^2 + 0^2) = 3          |
| 2   | sqrt(2^2 + 0^2 + 0^2) = 2          |
| 3   | sqrt(0^2 + 1^2 + 3^2) = sqrt(10)   |
| 4   | sqrt(0^2 + 1^2 + 2^2) = sqrt(10)   |
| 5   | sqrt((-1)^2 + 0^2 + 1^2) = sqrt(2) |
| 6   | sqrt(1^2 + 1^2 + 1^2) = sqrt(3)    |


- b) What is our prediction with K = 1? Why?

    Dado que nuestro vecino mas cercano es la observacion 5, cuyo valor es sqrt(2), y dicha observacion posee el valor
    "Green" para la variable respuesta, entonces nuestro modelo predice que  Y = "Green".


- c) What is our prediction with K = 3? Why?

    Nuestros 3 vecinos mas cercanos son: Observacion 5, 6 y 2. De estas, las observaciones 6 y 2 tienen un valor de
    "Red" para la variable de respuesta, mientras que la observacion 5 tiene un valor de "Green", Por lo tanto Y tiene
    probabilidad de 2/3 de pertenecer a la clase de "Red" y 1/3 de pertenecer a la clase "Grenn" por lo que el resultado
    es Y = "Red".


- d) If the Bayes decision boundary in this problem is highly non-linear, then would we expect the best value for K to
be large or small? Why?

    Si la frontera de decision de Bayes es altamente no lineal, entonces esperariamos que el mejor valor para K sea
    pequeño. Esto se debe a que un valor pequeño de K nos permite capturar mejor la complejidad del modelo, ya que
    estamos considerando un numero menor de vecinos cercanos. Si se considerara un numero K grande entonces el modelo 
    comenzaria a sesgarse hacia la clase mayoritaria, perdiendo la complejidad del modelo. Un ejemplo de esto se puede
    ver en el siguiente grafico extraido de la pagina 41 del libro ISLR:

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-intro-ml\KNN.png"/>