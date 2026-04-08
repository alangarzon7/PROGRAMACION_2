"""Tuplas
Una tupla es un tipo de secuencia similar a una lista, pero es inmutable, por lo que, una vez inicializada, no se puede cambiar ninguno de sus elementos sin generar un nuevo objeto.
Una tupla de Python comparte muchas propiedades con las listas:
● Puede contener varios valores en una sola variable
● Una tupla puede tener valores duplicados
● Está indexado: puede acceder a los elementos numéricamente

Tuplas vs Listas

● Una tupla es inmutable; No se puede cambiar una vez que la haya definido
● Una tupla se define usando paréntesis opcionales () en lugar de corchetes []."""
#ejemplo
tupla1 = (1,2,3,4,5)
print(type(tupla1))

#acceder a los elementos de una tupla

print(tupla1[2])

#no se pueden agregar ni quitar elementos d euna tupla, es INMUTABLE.
#LO QUE SI SE PUEDE: Crear una tupla nueva a partir d euna tupla anterior y agregarle elementos nuevos a la nueva.

tupla2 = (*tupla1,6,7)

print(tupla2)
