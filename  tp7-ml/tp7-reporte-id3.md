## A. Resultados sobre la evaluación sobre tennis.csv
El resultado obtenido aplicando el algoritmo de arboles de decision utilizando el dataset tennis.csv es el siguiente:

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\arbol_tennis.png"/>

## B. información sobre las estrategias para datos de tipo real

Cuando necesitamos tratar con valores continuos o reales en los atributos existen infinitos valores posibles para cada 
una de las instancias. Por lo tanto, existen diversas estrategias para tratar estos problemas, por ejemplo, se puede 
utilizar un punto de corte para dividir el intervalo y que este devuelva la mayor ganancia de informacion posible al 
modelo. Otra estrategia  es utilizar arboles de regression en lugar de arboles de clasificacion. En estos arboles, 
cada hoja posee una funcion lineal en vez de un valor de clase.