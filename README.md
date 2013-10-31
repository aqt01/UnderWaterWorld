UnderWaterWorld
===============

El planetaWa-Tor es un mundo acuático, toroidal y reticulado de dimensión 20x20.
 
Este mundo está habitado por peces y tiburones de ambos sexos. 

Cada habitante del mundo (pez o tiburón) esté representado por un hiloconcurrente.
 
Cada habitante del mundo nada desde la posición en que se encuentra una posición hacia el norte, sur, este u oeste 
(recuerde que el mundo es un toroide).
 
Si habitantes del mundo se encuentran en la misma posición ocurre lo siguiente:

a) si son del mismo sexo y de la misma especie, uno aniquila al otro. 
b) si son de especies diferentes, el tiburón siempre aniquila al pez.
c) si son de la misma especie y de distinto sexo, se reproducen, 
generando un nuevoindividuo cuyo sexo será macho o hembra con igual probabilidad, y luego continúan su camino.

Nota:

 configure.txt: Contiene la configuración sobre la cantidad de peces, tiburones y la configuración de las dimensiones
 de la ventana.

Librerías:

 Pyinstaller (para hacer el build) : http://www.pyinstaller.org/
 Pygame 1.9.1: 

Para ejecutar en linux, debe tener instalado pygame y solo tiene que "python game.py"

By: 
Aqt01 and Juan23 (https://github.com/Juan23) 
