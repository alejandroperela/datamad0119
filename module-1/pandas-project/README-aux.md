![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: Ataques de tiburón: de 1900 hasta nuestros días

## Descripción

En este proyecto he procedido a analizar los ataque de tiburones en todo el mundo desde el año 1900 hasta el día de hoy, visualizando en qué países ha habido más ataques y cuáles de ellos tienen la tasa de mortalidad más alta en caso de ataque. Para ello he realizado lo siguiente:

---

## Limpieza

1) Importo y visualizo los datos, y renombro las columnas para evitar cualquier tipo de error cuando trabaje con ellas y manipule los datos.
2) Analizo qué columnas tienen mayor número de nulos para, de una forma rápida, saber qué columnas es mejor ir eliminando. Así mismo, busco entre los datos duplicados para evitar analizar la misma información dos veces.
3) Sospecho que hay diversas columnas con información repetida, por lo que procedo a analizar en cuántas de las filas de dichas columnas hay datos repetido. Y dado que apenas hay diferencia entre una columna y otra, procedo a eliminar las columnas repetidas.
4) A continuación, y de forma muy relacionada con el paso anterior, procedo a eliminar el resto de columnas que considero poco relevantes para mi análisis.
5) Hecho esto, analizo las columnas con las que voy a trabajar para limpiar los posibles valores que no aporten información. Y para ello, sustituyo una serie de valores por otros que aportén más valor al análisis.
6) Una vez he limpiado el archivo, procedo a analizar la información contenida en él.


## Tratamiento de los datos

1)Dado que lo que quiero es analizar los ataque de tiburón en los siglos XX y  XXI, elimino los ataques que se hayan producido de forma anterior a esta fecha.
2) Empiezo analizando los países en los que ha habido más ataques, observando que los 5 países con más ataques son USA, Australia, South Africa, Papua New Guinea y Brazil.
3) En este primer escenario analizo cómo ha sido la distribución en porcentaje de los ataques según el sexo de la víctima, lo cual nos podría dar una aproximación de cual es la tendencia entre sexos a realizar actividades relacionadas con el mar. Como podemos observar, en USA el porcentaje de víctimas hombres fue del 80% mientras que el de mujeres fue del 15%. En el caso de Australia y de Sudáfrica los porcentajes fueron algo diferentes, siendo del 82% y 6% para Australia, y del 84% y 4% en el caso de Sudáfrica, debido al número de "Unkown" en estos dos países.
4) Aunque creo que el análisis anterior se queda un poco corto en cuanto a qué actividad realiza cada género, dado que la peligrosidad de cada una no es la misma. Y tras hacer los cálculos pertinentes, sabemos que la principal razón de los ataques a hombres fue el surf, mientras que en el caso de las mujeres fue por nadar.
5) Posteriormente paso a analizar los años para saber, desde 1900 hasta hoy, cuál ha sido el año con más ataques registrados. Y como podemos ver en los resultados, los años con más ataques han sido a partir de los 2000. Además, también analizo la razón más común del ataque según ha pasado el tiempo, agrupando los ataques por décadas y por género. De los resultados podemos concluir que la principal razón de los ataques hasta la década de los 80 fue por nadar, tanto para hombres como para mujeres. Es a partir de los 80 cuando la principal razón de los ataques a hombres es el surfing.
6) A continuación paso a analizar cómo han sido de graves los ataques por país, según si han sido mortales o no. Y continuo con las países que más ataques han registrado. En este caso, y a diferencia de antes, podemos observar que aunque USA es el país con más ataques, el país más mortífero en caso de ataque es Australia, siendo mortífero en un 31% de los casos, porcentaje muy parecido al de Sudáfrica, el cual es del 18%. Y aunque USA es el país con más ataques registrados, es el que menor tasa de muerte presenta, con un 11% de los casos.
7) Y por último he procedido a exportar el archivo limpiado.


## Lecciones y conclusiones

1) La importancia de tener una fuente de datos que produzca una información clara y ordenada, dado que reduce los errores y es mucho más fiable a la hora de tratar la información que si una persona la tratara directamente.
2) La importancia de tener datos y valores estandarizados para poder tratar la información de una forma más eficiente y poder extraer datos comprarables entre sí.





