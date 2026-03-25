"""Crear una función que reciba 3 notas, 
calcule el promedio y lo devuelva. """
def promedio(n1, n2, n3): 
    return (n1 + n2 + n3) / 3 
# Uso 
nota1 = float(input("Nota 1: ")) 
nota2 = float(input("Nota 2: ")) 
nota3 = float(input("Nota 3: ")) 
print("Promedio:", promedio(nota1, nota2, nota3))