"""Eliminar elementos del diccionario
Python nos provee varios métodos para eliminar elementos de un diccionario,
uno ya lo hemos mencionado que es el método del(). Vamos que otros métodos
tiene Python para ofrecernos 😀.

pop(): elimina el elemento con el nombre de clave especificado.
popitem(): este método elimina el último elemento insertado."""


auto = {"marca": "Renault",
        "modelo": "Koleos",
        "anio": 2014}

# Sacamos el modelo y lo guardamos antes de que se borre
modelo_eliminado = auto.pop("modelo")

print(f"Eliminé el modelo: {modelo_eliminado}")
print(auto) # Resultado: {'marca': 'Renault', 'anio': 2014}