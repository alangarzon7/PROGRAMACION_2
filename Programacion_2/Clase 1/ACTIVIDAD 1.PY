"""Actividad N° 1🤓

1. Crear una lista que contenga nombres de provincias
Argentinas, que contenga más de 5 elementos e imprimir por
pantalla
2. Imprimir por pantalla el tercer elemento de la lista
3. Imprimir por pantalla del segundo al cuarto elemento
4. Mostrar el tipo de dato de la lista
5. Mostrar los primeros 4 elementos de la lista
6. Agregar una provincia más a la lista que ya exista y otra que no.

7. Agregar una provincia, pero en la cuarta posición.
8. Extender otra lista a la ya creada.
9. Eliminar un elemento de la lista.
10. Extraer el último elemento de la lista, guardarlo en una variable e imprimirlo."""
provincias =["Tierra del Fuego", "Buenos Aires", "Mendoza", "San Juan","Salta"]
print(f"Estas son 5 provincias de Argentina {provincias}")
 
 #2. Imprimir por pantalla el tercer elemento de la lista
tercera=provincias[3]
print(f"Este es el tercer elemento de la lista: {tercera}")

#3. Imprimir por pantalla del segundo al cuarto elemento

segundoalcuarto=provincias[1:4]
print(f"Estos son del segundo al cuarto elemento: {segundoalcuarto}")

#4. Mostrar el tipo de dato de la lista
dato=type(provincias)
print(dato)

#. Mostrar los primeros 4 elementos de la lista
primeros4= provincias[:4]
print(f"Estos son los primeros 4 elementos : {primeros4}")

#6. Agregar una provincia más a la lista que ya exista y otra que no.
provincias.append("Tierra del Fuego")
provincias.append("Cordoba")
print(provincias)

#7. Agregar una provincia, pero en la cuarta posición.
provincias.insert(4,"Jujuy")
print(provincias)

#8. Extender otra lista a la ya creada
paises=["Argentina","Chile","Paraguay"]

provincias.extend(paises)

print(provincias)

#9. Eliminar un elemento de la lista.

provincias.pop(1) 
print(provincias)

#10. Extraer el último elemento de la lista, guardarlo en una variable e imprimirlo

ultimo_elemento= provincias.pop()
print(f"El elemento eliminado fue : {ultimo_elemento}")