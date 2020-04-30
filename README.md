# Covid-19
Interfaz web sobre los casos del Covid-19 en la Región de Madrid, utilizando la librería Dash de plotly.

Esta puede ser de utilidad para poder ver la evolución de los casos de Covid-19, y posibles fallos en la recogida de datos (ej. caso de La Hiruela, que recoge la tasa acumulada más alta de la Comunidad de Madrid y se mantiene constante en el tiempo).
En ella podemos hacer uso del dropdown para seleccionar entre los casos disponibles en la Comunidad de Madrid.
* Casos confirmados en los últimos 14 días.
* Total casos confirmados en los últimos 14 días.
* Tasa de incidencia acumulada.
* Tasa de incidencia acumulada total.
Así como también se puede hacer uso del Slider para seleccionar el día a visualizar.
En cuanto a la serie temporal, encontramos que de inicio solo se visualiza el total de la Comunidad de Madrid, pero clicando encima de los nombres de los distritos podemos agregarlos/desagregarlos para poder comparar los datos entre ellos. También podemos visualizar los datos posicionando el ratón encima de la gráfica que hará aparecer un cuadro con los datos.
Finalmente encontramos un cuadro con los registros máximos encontrados en los últimos 14 días y el municipio en el que se han producido.

Para poder hacer uso del ```<iframe>``` primero hay que correr el archivo Embed_Interfaz.py para crear las visualizaciones en localhost. 
Luego esta se vuelca en el archivo ReactivaMadrid.html. 

## Librerías implementadas:
* werkzeug
* flask
* dash
* plotly
* pandas
* geojson
