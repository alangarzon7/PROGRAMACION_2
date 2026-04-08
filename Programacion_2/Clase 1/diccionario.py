# Creación
telefonos = {
    'Gonzalo': 12345678,
    'Pedro': 986455882,
    'María': 445566887
}

# Para buscar un dato, usamos corchetes con la CLAVE
numero_maria = telefonos['María']
print(f"El numero de Maria es {numero_maria}")

#para agregar

telefonos['Veronica'] =1293952359034
print(telefonos)

#para eliminar

del(telefonos['Gonzalo'])
print(telefonos)

#sobreescribir entrada, simplemenrte asignamos un nuevo valor, no es  necesario eliminar
telefonos1 = {
    'Gonzalo': 12345678,
    'Pedro': 986455882,
    'María': 445566887
}
telefonos1['Gonzalo'] =11111111111
print(telefonos1)

#SUBDICCIONARIO

usuario = {
    "nombre": "Alan",
    "redes_sociales": ["@alan_dev", "@alan_ig"], # Una lista
    "direccion": {                               # Un sub-diccionario
        "ciudad": "Rio Grande",
        "provincia": "Tierra del Fuego"
    }
}