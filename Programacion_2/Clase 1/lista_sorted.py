"""Usando Sorted
La diferencia entre el método sort y sorted, es que mientras sort modifica la lista original,
sorted crea una nueva lista, sin alterar la lista original. De esta manera yo podría usar una
variable para almacenar el resultado de sorted, y de esta manera tendría dos listas, la original
y la ordenada."""
lista1=[10,15,2,4,1]
lista_ordenada=sorted(lista1)

print(lista1)

print(lista_ordenada)

#descendente
lista_ordenada_descendente=sorted(lista1,reverse=True)
print(lista_ordenada_descendente)
