- a. Cual es la distribución de las clase inclinacion_peligrosa?

Dentro de la particion del dataset que creamos nos encontramos con una distribucion bastante desbalanceada entre las 2
posibles clases de inclinacion_peligrosa. La clase 0 (no peligroso) tiene casi 8 veces mas elementos que la clase 1
(peligroso).

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\distribucion.png"/>

- b. ¿Se puede considerar alguna sección más peligrosa que otra?

Basado en los datos encontrados en el dataset, podemos ver que la seccion con mayor cantidad de arboles con inclinacion
peligrosa es la seccion 4 (Cuarta Oeste), ya que en ella se encontraron mas de 750 arboles con inclinacion peligrosa.
Mientras que en el resto de secciones se encuentran entre 500 para abajo.

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\secciones_peligrosas.png"/>

- c. ¿Se puede considerar alguna especie más peligrosa que otra?

Se puede observar que la especies mas peligrosa segun los datos dentro del dataset son las moreras (1er imagen). Sin 
embargo, esto tambien se puede deber a que la morera es el arbol mas predominante en el dataset (2da imagen). si 
analizamos la proporcion de arboles de cada especie en relacion a la cantidad de arboles con inclinacion peligrosa de 
cada especie(3ra imagen), podemos ver que la especie mas peligrosa es el algarrobo seguido por la morera. Es importante
aclarar que dentro del dataset utilizado, solo nos encontramos con 3 instancias de algarrobos, por lo cual no es una 
muestra representativa.

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\especies_peligrosas.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\especies.png"/>
<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\peligrosidad_por_especie.png"/>

---

3. A partir del archivo arbolado-mendoza-dataset-train.csv

- a. Generar un histograma de frecuencia para la variable circ_tronco_cm. Probar con diferentes números de bins.

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\frecuencia_circ_tronco.png"/>

- b. Repetir el punto 1) pero separando por la clase de la variable inclinación_peligrosa?

<img src="C:\Users\Facu\PycharmProjects\ia-uncuyo-2023\ tp7-ml\graficos\peligrosidad_circ_tronco.png"/>

- c. Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir  circ_tronco_cm, en donde puedan 
asignarse solo 4 posibles valores [ muyalto, alto, medio, bajo ]. Utilizar la información del punto a. para seleccionar 
los puntos de corte para cada categoría. Guardar el nuevo dataframe bajo el nombre de 
arbolado-mendoza-dataset-circ_tronco_cm-train.csv

El criterio de seleccion de los puntos de corte fue utilizar los cuartiles de la variable circ_tronco_cm. De esta forma
se obtuvieron los siguientes puntos de corte: 0.2, 60, 110, 156 y 500. Dando como resultado los siguientes intervalos 
para cada claisificacion: [0.2, 60), [60, 110), [110, 156), [156, 500].

