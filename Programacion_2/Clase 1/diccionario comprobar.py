#Comprobar si existe una clave en un diccionario
#Podemos comprar si existe una clave dentro de un diccionario con las palabras claves in y not in:
#creo otro diccionario con subdiccionario
# Creamos el diccionario con la clave 'lista1'
diccionario = {
    'sub_diccionario': {'a': 30, 'b': False},
    'lista1': [10, 20, 30]
}

# --- LA COMPROBACIÓN ---

# Pregunta 1: ¿Está la clave 'lista1' en el diccionario?
print('lista1' in diccionario) 
# Resultado: True (Porque sí existe esa etiqueta)

# Pregunta 2: ¿NO está la clave 'lista1' en el diccionario?
print('lista1' not in diccionario) 
# Resultado: False (Porque es mentira que no está; ¡vimos que sí está!)