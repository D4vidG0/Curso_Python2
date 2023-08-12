# Tarea 2 Visualizacion de datos de API juego Dota 2

## <h1>Introduccion</h1>

Este programa se basa en las funciones creadas en la Tarea 1. Se modificaron dichas funciones para mostrar los datos que me parecieron interesantes. Dichas funciones se encuentran en el archivo Tarea1.py, el cual se importo como modulo en el main. 

Tambien se crearon las funciones nuevas para graficar en el main y presentan datos que pueden servir para saber el impacto del juego a nivel mundial y tambien para ayudar a los jugadores nuevos a seleccionar personajes dentro del juego.

A continacion se detallan los datos que se seleccionaron, asi como las graficas que decidi mostrar.

## <em><strong>Datos seleccionados</strong></em>.

Los datos que seleccione fueron por ejemplo: velocidad, fuerza, agilidad, inteligencia; los cuales son atributos que pueden servir para seleccionar un heroe a la hora de jugar el juego. Inclusive hay jugadores que no saben estos datos, ya que no se presentan de forma facil en el juego. Tambien escogi mostrar el pais con mayor cantidad de jugadores y el pais con menor cantidad de jugadores ya que me parecio interesante. 

Tambien un dato muy importante es el MMR que es el numero que indica el nivel de cada jugador, y entre mas alto sea, mejor es el nivel del jugador. Dicho esto, escogi mostrar el MMR promedio mundial, esto quiere decir que ese numero es el nivel promedio de cada jugador en todo el mundo. 

Quise mostrar la cantidad de jugadores que hay en el mundo de este juego, y como se puede observar es una buena base de jugadores.

Por ultimo, queria mostrar los datos especificamente de Costa Rica (cantidad de jugadores y nivel MMR promedio). Como podemos observar, los jugadores ticos presentan un nivel promedio del juego. 

## <em><strong>Grafica de Top 10 de paises con mas jugadores</strong></em>.

Como el API regresaba mucha informacion, decidi mostrar los top 10 o top 5 de datos para que fuera mas comprensible. En esta grafica especifica, se muestran los 10 paises con mayor cantidad de jugadores. Esto es interesante, ya que con esta informacion se puede saber cuales servidores tienen la mayor cantidad de servidores y asi sabemos cuales estan mas congestionados. 

## <em><strong>Grafica de top 5 de paises con mejores jugadores</strong></em>.

Aca se muestran los paises donde estan los mejores jugadoes del mundo. Esta nos sirve para ver en cuales servidores son donde estan los mejores jugadores (normalmente el servido de Asia), y ver repeticiones de esa zona del mundo y asi poder mejorar en el juego. 

## <em><strong>Grafica de heroes con mayor fuerza.</strong></em>.

Esta grafica la que quise meter, ya que el atributo de fuerza esta relacionado con la cantidad de vida que tenga ese heroe en el juego. Entonces entre mayor fuerza, mayor cantidad de vida posee ese personaje. Para los jugadores nuevos, este dato puede ser importante ya que presenta los heroes con mayor vida al inicio del juego entonces asi puede seleccionar uno de estos y evitar que los maten mas seguido.

## <em><strong>Funcionamiento</strong></em>.

Se crearon los menus tipicos para seleccionar los datos que se desean. Lo unico diferente es que si se selecciona una grafica, se debe cerrar la grafica para poder regresar a las opciones del menu. 