"""Situación: El programa debe pedir al usuario 4 notas 
(una por una), sumarlas y calcular el promedio final. 
Mostrar el promedio al finalizar."""
suma = 0 
for i in range(4): 
    nota = float(input(f"Ingrese la nota #{i + 1}: ")) 
    suma += nota 
promedio = suma / 4 
print("El promedio es:", promedio) 