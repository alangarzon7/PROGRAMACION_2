"""Explorar valores de diccionarios
Una vez que tenemos creado el diccionario, las operaciones para explorar
los diccionarios son las siguientes:

keys(): devuelve un objeto tipo dict_view del diccionario con las claves que contiene."""

telefonos = {
    'Gonzalo': 12345678,
    'Pedro': 986455882,
    'María': 445566887
}
#keys(): devuelve un objeto tipo dict_view del diccionario con las claves que contiene.
print(telefonos.keys())

#values(): devuelve un objeto de tipo dict_values del diccionario con los valores que contiene.
print(telefonos.values())

#items(): devuelve un objeto de tipo dict_items del diccionario con los pares clave-valor
# de los elementos presentes en el diccionario.
print(telefonos.items())

#get(): devuelve el valor asociado a la clave. Si no lo encuentra, devuelve None. Si se añade un valor
# por defecto y no encuentra la clave pedida, devuelve el valor por defecto.
print(telefonos.get('Gonzalo'))

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