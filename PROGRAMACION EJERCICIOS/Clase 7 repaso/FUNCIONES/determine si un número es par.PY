"""Crear una función que reciba un número y 
devuelva True si es par, False si es impar. """
def es_par(numero): 
    return numero % 2 == 0 
# Uso 
n = int(input("Ingrese un número: ")) 
if es_par(n): 
    print("Es par") 
else: 
    print("Es impar") 