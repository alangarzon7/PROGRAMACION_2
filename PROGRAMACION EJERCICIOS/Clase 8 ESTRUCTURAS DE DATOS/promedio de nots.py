notas = [5, 8, 9, 6]
suma = 0  #para sumar todos los valores de la lista
for nota in notas:
    suma +=nota
promedio= suma / len(notas)  #El len esta tomando la longitud de la cantidad de ELEMENTOS que tiene la lista notas
"""print(f"Promedio: {promedio}")"""

if promedio >=6:
    print(f"Nota: {promedio}...Aprobado")
else:
     print(f"Nota: {promedio}..desaprobado")