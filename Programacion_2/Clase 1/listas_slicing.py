"""Hay veces que necesitamos obtener partes de una lista. Python como ya lo vimos con las cadenas (strings) tiene una sintaxis para poder cortar, rebanar o segmentar una lista.

La sintaxis de segmentación es la siguiente:
mi_lista[inicio:fin:paso]
con respecto a esta sintaxis podemos detallar lo siguiente:
● inicio: es la primera posición del elemento que se incluye.

● fin: es exclusivo, lo que significa que el elemento en la posición fin no se incluirá.

● paso: es el tamaño del paso es decir si los elementos van a ir buscando de 1 en 1 desde
el inicio o de 2 en 2, etc.

● inicio, fin y paso son todos opcionales.

● También se pueden usar valores negativos."""

lista1=[1,2,3,4,5,6,7,8]
lista1[0:3]  #Muestra los primeros 3 elementos de la lista

lista1[:3]  #comienza desde el rpimer elemento de la lista en la posicion 0

lista1[4:]  #Comienza en el elemento indice 4 y va hasta el final de la lista

lista1 [::2] #va desde el inicio hasta el final de la lista, recorriendo de 2 en 2