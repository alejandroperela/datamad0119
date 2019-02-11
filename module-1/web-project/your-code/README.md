![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Guided Project: API and Web Data Scraping

## Proyecto

El principal propósito de este proyecto es obtener una lista de citas célebres, junto con su autor y con las caractéristicas de la cita, como el tipo de cita que es. Esta información la obtendres haciedno web scraping de la web "https://www.azquotes.com/top_quotes.html", la cual contiene exactamente 1000 citas célebres.

A partir de ahí la idea es utilizar la API de Wikipedia para obtener información respecto al autor de cada cita. Y una vez la haya conseguido, juntar ambas bases de datos para hacer una más grande y enriquecida.

Respecto a la estructura del mismo, aunque inicialmente tenía pensado emplear una API para obtener información, y con esa información recorrer diferentes dominios para enriquecerla, he creído mejor para este caso empezar obteniendo un dataset de un único dominio, asegurando que toda la información esté relacionada y sea del mismo tipo, y así emplear un único código. Y una vez haya sacado la información, utilizar la API para enriquecerla, ya que con dicha API la información que obtenga será toda del mismo sitio y el input para hacer la búsqueda ya lo tengo del Web Scraping.



## Código

En la primera casilla incluyo las librería y paquetes con los que voy a ir trabajando



## Web scraping

En la celda de debajo he escrito el código con el que obtengo las citas con sus respectivo autores y tags, rotando por cada una de las 10 páginas de la web a través del loop for. Una vez tengo toda la información que quiero, la junto utilizando un diccionario, y la convierto en un DataFrame de 4 columnas, incluyendo el índice, el cual he formateado para que empiece por 1, en vez de 0.

Respecto a los autores, dado que en la posterior aplicación de la API de Wikipedia aparecían algunos errores de desambiaguación, he cambiado algunos nombres antes de meterlos en la lista de autores con el nombre que no me diese error.



## Wikipedia API

A continuación, utilizo la API de Wikipedia para ir rotando por la lista de autores de cada una de las citas para obtener un breve resumen con la biografía del autor y el link con el resto de la información en Wikipedia. Según sacamos la información, la incluimos en una lista que posteriormente convertiremos a DataFrame. 

Wikipedia me devolvía, aparte de la breve biografía, dos veces el nombre y el link de la página de Wikipedia, por lo que únicamente me he quedado con el tercer elemento de la lista, es decir, de la biografía.

Ahora juntamos ambos datasets para crear una base de datos más grande y más enriquecida. Como podemos observar, la columna de la derecha corresponde con la información del autor extraida de la Wikipedia.



## Twitter API

He decidido utilizar una segunda API para saber cómo de populares son en la actualidad los autores de las citas, obteniendo tweets clasificados como populares que contengan el nombre del autor. Una cosa importante a la hora de trabajar con esta API es que sólo puedes hacer 180 peticiones cada 15 minutos, por lo que he tenido que hacer 6 peticiones para buscar todos los autores.

La fórmula funcionaba porque la he utilizado para obtener el número de tweets populares sobre Alex Txikon (un escalador español), Himalaya, Esperanza Aguirre y Colón, y me daba cantidades de alrededor de 4 y 25, bastante razonables.

Dado que no puedo hacer la petición para todo mi DataFrame, dejo puesta la fórmula completa.



## Translate API

Con la siguiente API (https://pypi.org/project/translate/) lo que pretendo es traducir cada una de las citas al español. Aunque el funcionamiento de esta API se basa en funciones y no en peticiones que se hacen a una URL tal como en el caso de la Wikipedia. Esta API, al igual que la anterior, tiene un límite de uso cada x tiempo que ahora mismo no conozco.

Para ello, y de forma similar a la anterior API, trabajo con un bucle que para cada cita me haga la traducción del inglés al español. Y como antes, inserto el resultado en un DataFrame que posteriormente fusiono con las dos bases de datos anteriores.



## Obstáculos encontrados

Creo que el principal obstáculo que me he encontrado ha sido el trabajar con la API de WIkipedia, ya que inicialmente empecé trabajando con una variante de la misma que funcionaba a través de funciones, y la cual tardaba mucho en cargar la información. Fue posteriormente cuando descubría la otra variante y que esa más rápida.

Aparte de eso, el resto de obstáculos han sido pequeños y simplemente ha sido cuestión de investigar un poco.



## Lecciones aprendidas

Una de las principales lecciones que he aprendido ha sido saber lo importante que es escoger la web correcta sobre la que vas a hacer web scrapping.

Y la otra es el haber aprendido a trabajar con APIs, saber qué inputs son necesarios y saber de dónde sacarlos.