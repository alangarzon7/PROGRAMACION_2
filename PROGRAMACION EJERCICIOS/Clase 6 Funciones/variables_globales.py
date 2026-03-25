"""
---Definidas fuera de cualquier función.

---Accesibles en todo el programa.

---Compartir datos entre múltiples funciones."""

x = 10  # Variable global

def mi_funcion():
    print(x)

mi_funcion()  # Output: 10
print(x)  # Output: 10

#se aconseja usar las variables locales