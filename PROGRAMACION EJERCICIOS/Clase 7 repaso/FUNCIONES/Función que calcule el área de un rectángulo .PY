"""Situación: Crear una función que reciba base y altura 
y devuelva el área del rectángulo. 
"""
def calcular_area(base, altura): 
    return base * altura 
# Uso 
b = float(input("Ingrese la base: ")) 
h = float(input("Ingrese la altura: ")) 
print("El área es:", calcular_area(b, h))


