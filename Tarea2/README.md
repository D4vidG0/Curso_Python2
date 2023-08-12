# Tarea 1 Consumo de datos de API

## Introduccion

Este programa es para la api Open Dota, la cual brinda datos del videojuego Dota 2. Esta Api ofrece 50 000 calls por mes y brinda datos como MMR, paises donde se juega el juego, datos de los heroes que presenta el juego, datos de los equipos profesionales del juego e inclusive se pueden sacar datos de partidas individuales ya sean privados o publicas. 

El MMR es un numero que indica el nivel de cada jugador, entre mas alto sea este numero, mejor posicionado esta el jugador en el ranking mundial. 

La documentacion de la API se encuentra en el siguiente link:

https://docs.opendota.com/

## Consumo de datos de la API

Se crearon 8 funciones para extraer los datos que me parecieron mas interesantes de esta API y que podrian servirle a los jugadores. Las funciones que se crearon fueron para extraer los datos como: nombre de todos los heroes, estadisticas de cada heroe, paises donde se juega el juego Dota 2 y MMR promedio de cada pais. A continuacion, se detalla cada endpoint que se extrajo. 

### Nombres de los Heroes

Con esta funcion, se muestra todos los nombres de cada heroes que presenta el juego. El juego presenta 123 heroes en total, divido en 4 categorias: Fuerza, agilidad, inteligencia y universal. 

### Movimiento de los Heroes

Con esta funcion se obtiene la velocidad de movimiento al principio del juego para cada heroe. El numero que se presenta es la velocidad base con la que empieza el heroe y entre mas grande sea el numero, mas rapido se movera por el mapa dicho heroe. 

### Roles de cada heroe del juego

Esta funcion detalla los roles de cada heroes del juego. Los roles principales son: Carry y Support. Existen otros subroles como: Initiator', 'Durable', 'Disabler', 'Nuker, los cuales se catalogan dependiendo de las habilidades de cada heroe. 

### Estadisticas de cada heroe

Se crearon 3 funciones para obtener las estadisticas principales de cada heroe. Las 3 estadisticas principales son: Fuerza, agilidad e inteligencias. Las 3 funciones que se crearon muestran por separado la fuerza, agilidad e inteligencia con la que empieza cada heroe. 

### Numero de jugadores de cada pais

Otro dato que me parecio relevante es el numero de jugadores de cada pais, por ello cree la funcion que extryera este dato. Y la funcion muestra el numero total de jugador por cada pais del mmundo. 

### MMR promedio de cada pais

Esta funcion obtiene el MMR promedio de cada pais. Como mencione antes, el MMR es el numero que se le asigna a cada jugador y se gana jugando partidas rankeadas del juego. Entre mas alto, mejor es el jugador. 

## Graficas

Algunas de las graficas que se pueden obtener de estos datos son:

1. country vs average mmr
2. country vs number of players
3. heroe vs move speed
4. heroe vs str
5. Heroe vs int
6. Heroe vs agi

De esta manera se pueden mostar de manera mas comprensible los datos. 