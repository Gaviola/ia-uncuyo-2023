A) Ejecutar cada uno de los algoritmos implementados en la parte I 30
veces y calcular para el caso de 4, 8,10,(12,15)? reinas:
1. El número (porcentaje) de veces que se llega a un estado de
solución óptimo.
2. El tiempo de ejecución promedio y la desviación estándar para
encontrar dicha solución. (se puede usar la función time.time() de
python)
3. La cantidad de estados previos promedio y su desviación estándar
por los que tuvo que pasar para llegar a una solución.
4. Generar un tabla con los resultados para cada uno de los algoritmos
desarrollados y guardarla en formato .csv (comma separated value)
5. Realizar un gráfico de cajas (boxplot) que muestre la distribución de
los tiempos de ejecución de cada algoritmo. (ver gráfico de ejemplo)
---
***Resultados:***

**Tamaño = 4**

***Hill Climbing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 33%

2- Media y Desviación Estandar del Tiempo de Ejecución

    μ = 0.00023314952850341796 Segundos 
    
    σ = 0.0004298443154616735 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 27.6 Estados 
    
    σ = 8.426558998293677 Estados

***Simulated Annealing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 100%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 0.0007329940795898438 Segundos 
        
    σ = 0.0005830020812328793 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados
    
    μ = 72.93333333333334 Estados 
        
    σ = 35.46531412164745 Estados

***Algoritmo Genético***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 100%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 0.0026654799779256186 Segundos 
        
    σ = 0.003164370415190203 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 2.033333333333333 Estados 
        
    σ = 3.6717310897453124 Estados

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Costo_Tamaño_4.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Tiempo_Tamaño_4.png"/>

---
**Tamaño = 8**

***Hill Climbing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 10%

2- Media y Desviación Estandar del Tiempo de Ejecución

    μ = 0.0033983866373697917 Segundos 
    
    σ = 0.0008939011639346998 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 231.46666666666667 Estados 
    
    σ = 63.651927041464766 Estados

***Simulated Annealing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.9666666666666667%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 0.011794288953145346 Segundos 
        
    σ = 0.010650785776671069 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados
    
    μ = 741.1666666666666 Estados 
        
    σ = 697.8111138228687 Estados

***Algoritmo Genético***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.26666666666666666%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 3.734449521700541 Segundos 
        
    σ = 2.1177482005228976 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 2251.0666666666666 Estados 
        
    σ = 1275.8103289291473 Estados

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Costo_Tamaño_8.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Tiempo_Tamaño_8.png"/>

---

**Tamaño = 10**

***Hill Climbing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.03333333333333333%

2- Media y Desviación Estandar del Tiempo de Ejecución

    μ = 0.00956257184346517 Segundos 
    
    σ = 0.0031461737692805923 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 429 Estados 
    
    σ = 112.56722129618741 Estados

***Simulated Annealing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.8%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 0.03411637147267659 Segundos 
        
    σ = 0.02224078772843976 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados
    
    μ = 1465.1666666666667 Estados 
        
    σ = 1016.5216582096002 Estados

***Algoritmo Genético***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.23333333333333334%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 5.705535364151001 Segundos 
        
    σ = 2.6071373407982787 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 2445.0333333333333 Estados 
        
    σ = 1119.8130226725918 Estados

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Costo_Tamaño_10.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Tiempo_Tamaño_10.png"/>

---

**Tamaño = 12**

***Hill Climbing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.1%

2- Media y Desviación Estandar del Tiempo de Ejecución

    μ = 0.024321508407592774 Segundos 
    
    σ = 0.007256750273773908 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 814 Estados 
    
    σ = 130.08962427813984 Estados

***Simulated Annealing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.7666666666666667%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 0.048243506749471025 Segundos 
        
    σ = 0.03168142153948401 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados
    
    μ = 1509.0333333333333 Estados 
        
    σ = 1005.1163419821311 Estados

***Algoritmo Genético***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.13333333333333333%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 8.64556630452474 Segundos 
        
    σ = 2.9496549962854592 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 2662.633333333333 Estados 
        
    σ = 886.951675522767 Estados

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Costo_Tamaño_12.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Tiempo_Tamaño_12.png"/>

---

**Tamaño = 15**

**Tamaño = 12**

***Hill Climbing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.03333333333333333%

2- Media y Desviación Estandar del Tiempo de Ejecución

    μ = 0.07573034763336181 Segundos 
    
    σ = 0.019092519277168804 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 1456 Estados 
    
    σ = 233.54243504236493 Estados

***Simulated Annealing***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.5333333333333333%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 0.11311283906300863 Segundos 
        
    σ = 0.05026829502692411 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados
    
    μ = 2220.5666666666666 Estados 
        
    σ = 940.7848771411408 Estados

***Algoritmo Genético***

1- Soluciones Encontradas

    Porcentaje de soluciones óptimas: 0.06666666666666667%

2- Media y Desviación Estandar del Tiempo de Ejecución
    
    μ = 14.531390404701233 Segundos 
        
    σ = 2.901256107845817 Segundos
3- Media y Desviación Estandar de la Cantidad de Estados

    μ = 2880.5 Estados 
        
    σ = 543.2434362553153 Estados

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Costo_Tamaño_15.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\tp5-busquedas-locales\boxplots\Tiempo_Tamaño_15.png"/>

---

B) Para cada uno de los algoritmos, graficar la variación de la función h() a
lo largo de las iteraciones. (Considerar solo una ejecución en particular)

Los resultados se pueden apreciar en los graficos previamente mostrados en el punto A)

C) Indicar según su criterio, cuál de los tres algoritmos implementados
resulta más adecuado para la solución del problema de las n-reinas.
Justificar.

Basado en los resultados obtenidos ejecutando 30 veces, con un maximo de 3000 estados recorridos, cada algoritmo con sus respectivos tamaños (4,8,10,12,15),
Se puede concluir que el algoritmo mas adecuado para la resolucion del problema de las n-reinas es el algoritmo
de anneling. Esto se debe a que fue el que garantizo encontrar la solucion optima en la mayoria de las ocasiones en un tiempo
bastante razonable, en relacion a los resultados obtenidos comparado a los otros 2 algoritmos. Hill Climbing podria utilizarse 
en algun caso donde se busque una solucion relativamente buena en un tiempo corto, pero no es recomendable para encontrar la 
solucion optima ya que generalmente es proclive a quedarse en un maximo/minimo local. El algoritmo genetico, por otro lado, 
obtuvo los peores resultados en lo que respecta a tiempo de ejecucion y cantidad de estados recorridos, aunque supero a 
Hill Climbing a la hora de obtener resultados optimos. Puede ser una opcion valida si se retocan ciertos parametros y el
tiempo no es nuestra prioridad.
