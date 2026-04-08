#1. Crear una tupla que contenga los números enteros del 1 al 20
numeros = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#tambien se puede hacer con range:
#numeros = tupla(range(1,21))  hasta 21 pq el limite superior es exclusivo, lelga hasta 20

#2. Imprimir desde el índice 10 al 15 de la tupla
print(numeros[10:15])

#3. Mostrar la cantidad de veces que se encuentra un elemento específico
# dentro de la tupla y de la lista (utilizar count)
ocurrencia = numeros.count(5)
print(f"El numero 5 aparece {ocurrencia} veces en la tupla")

#4. Convertir la tupla en una lista
lista_convert = list(numeros)
print(type(lista_convert))
print(lista_convert)

#5. Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
uno, dos, tres,*resto =numeros
print(f"Variable uno: {uno}")
print(f"Variable dos: {dos}")
print(f"Variable tres: {tres}")
#ecesitas usar el asterisco * para "atrapar" el resto, o de lo contrario Python te dará un error.