"""2. Contar vocales en una palabra """
def contar_vocales(palabra): 
    contador = 0 
    for letra in palabra: 
        if letra.lower() in "aeiou": 
            contador += 1 
    return contador 
 
cantidad = contar_vocales("murciélago") 
print(cantidad)