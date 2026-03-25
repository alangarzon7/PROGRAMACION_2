"""Verificar si una palabra es palíndromo """

def es_palindromo(palabra): 
    invertida = "" 
    for i in range(len(palabra) - 1, -1, -1): 
        invertida += palabra[i] 
    return palabra == invertida 
 
resultado = es_palindromo("reconocer") 
print(resultado) 