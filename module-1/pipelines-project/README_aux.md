![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: Web Data Pipeline

## Overview

En este proyecto, voy a analizar diferentes características básicas de todos los países del mundo, con el fin de poder ver las diferencias entre ellos en las principales magnitudes de libertad, y cómo han evolucionado estas en el tiempo.

EL informe oficial completo se puede encontrar en el siguiente enlace: https://object.cato.org/sites/cato.org/files/human-freedom-index-files/human-freedom-index-2018-revised.pdf


## Acquisition

A través de Kaggle, he descargado el archivo "The Human Freedom Index", el cual muestra una medida global de la libertad personal, civil y económica.

Una vez descargado el archivo, a través de Jupyter Notebook lo he abierto para empezar a trabajar en él.


## Wrangling

Procedo a ver las columnas que tiene y qué información contiene cada una. Para esto me he apoyado principalmente en Kaggle y en la descripción que hacen de cada columna.

A traveś de Python me voy quedando con las columnas que más me interesan, y les cambio el nombre para hacer más legible el archivo. Las columnas serían las siguientes.
    Civil_justice
    Freedom_of_association
    Freedom_of_expression
    Same_sex_relationships
    Personal_Freedom
    Economic_Freedom
    Human_Freedom
    
Una vez tengo las columnas que quiero, veo si existe algún elemento duplicado, aunque como era de esperar, no hay ninguno.

Posteriormente miro las filas que tengan NaN's para deshacerme de ellas.

Y para terminar elimino las columnas que sean nulas y guardo el archivo csv limpiado.



## Analysis

A partir de aquí empiezo a seleccionar la información con la que me quiero quedar. En este caso, con información del año 2016, el último año disponible, para saber cuales fueron los países con mayor y menor libertad, medido en la columna Human Freedom.

Así mismo, hago un breve resumen de las características de las principales métricas de ambos grupos para, a través de un simple vistazo, ver la principales diferencias.

En las dos últimas tablas selecciono únicamente la Justicia Civil y la Libertad, ya que son los dos campos que más me interesan, uso el año como index, y muestro la media para los 5 mejores y 5 peores países según el ranking.

Y eso ahora cuando empiezo a hacer el anaĺisis de los 3 países que me interesan de este dataset, que son Nueva Zelanda, por ser el número 1, Venezuela por ser el último, y España por ser mi país.

Lo que voy a hacer es ver la evolución de la Libertad Total y de la Justicia Civil a lo largo de los últimos 8 años, viendo la variación entre años y entre 2008 y 2016.

También hago un gráfico de barras para mostrar de forma gráfica la evolución de la variable total de Libertad.

Y termino el análisis anual midiendo lo que han variado las variables Justicia Social y Libertad Humana a lo largo de los últimos años para cada uno de los 3 países.

A continuación, y para arrojar más luz sobre el análisis, voy a ver cómo ha sido la correlación entre la Justicia Civil y la Liberta durante los últimos 8 años, de forma general para todos los países, y para cada uno de los países que estoy analizando.

Así mismo miro también a la correlación entre el paso del tiempo y la Libertad, para confirmar si con el tiempo, los países tienden a ser más libres.

En este paso hago una matriz de correlación para saber cómo se relaciona cada variable con el resto, y un mapa de calor de correlaciones, para tener una interpretación más gráfica y visual.

Para ir terminando con mi análisis, me gustaría analizar más en profundidad el caso de Venezuela, dado que es uno de los países que más cambia, y más presentes en los medios nacionales.

Por ello, he analizado la tendencia pasada para hacer una estimación de cómo va a ser el indicador de Libertad en el próximo año 2017 a través de dos gráficas que han seguido diferentes metodologías.



## Reporting

Procederé a enviar un email con toda la información de forma anual, de acuerdo a la frecuencia con la que salen los datos.



## Conclusiones

Una de mis principales conclusiones sería que aún existe mucha diferencia entre los principales países más desarrollados y lo menos desarrollados, dando para los primeros unas métrica de JUsticia Social y de Libertad Humana de 7.8 y 8.7, y para los segundos unos índices de 4 y 5 respectivamente. Una cosa que me ha sorprendido mucho ha sido la poco correlación entre el paso del tiempo y la mejora de las libertades. A priori cabría esperar que con el paso del tiempo éstas mejorasen, pero en la práctica se han mantenido prácticamente estables. Respecto al resto de correlaciones, éstas varían entre 0.25 y 0.8.

Respecto a los 3 países que hemos analizado, tanto Nueva Zelanda como España han evolucionado muy poco a lo largo de los años:
La variación ANUAL de Civil_justice y de Human_Freedom en New Zealand durante los últimos 8 años ha sido respectivamente de un 0.45%, y de un -0.03%.
La variación TOTAL de Civil_justice y de Human_Freedom en New Zealand entre 2008 y 2016 ha sido respectivamente de un 3.65%, y de un -0.26%.

La variación ANUAL de Civil_justice y de Human_Freedom en Spain durante los últimos 8 años ha sido respectivamente de un 0.27%, y de un -0.13%.
La variación TOTAL de Civil_justice y de Human_Freedom en Spain entre 2008 y 2016 ha sido respectivamente de un 2.18%, y de un -1.07%.

La variación ANUAL de Civil_justice y de Human_Freedom en Venezuela durante los últimos 8 años ha sido respectivamente de un -1.79%, y de un -2.77%.
La variación TOTAL de Civil_justice y de Human_Freedom en Spain entre 2008 y 2016 ha sido respectivamente de un -13.48%, y de un -20.11%.

A la vista de estos resultados, podemos observar que es Venezuela la que más cambia. A lo largo de los últimos 8 años, ha visto caer sus libertades de una forma importante. Y en el posterior análisis gráfico en el que hemos intentado predecir cómo será el siguiente año en cuanto a métricas de libertad, podemos ver que ambas gráficas muestra que la tendencia de restricción de libertades continuará, dando índices de entre 3.8 y 4.1.




