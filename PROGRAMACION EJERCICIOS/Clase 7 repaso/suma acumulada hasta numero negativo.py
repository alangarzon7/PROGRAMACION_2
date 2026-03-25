"""Situación: Pedir números al usuario uno por uno e ir 
sumándolos. 
El programa debe continuar mientras los números sean 
positivos (mayores o iguales a 0). 
Cuando se ingrese un número negativo, se detiene y 
muestra la suma total."""

suma=0
numero=int(input("iNgrese un numero(negativo para terminar): "))
while numero>=0:
    suma+=numero
    numero=int(input("iNgrese un numero(negativo para terminar): "))
print(f"La suma total es {suma}")
