"""  ---Definidas dentro de una función.

     ---Accesibles solo dentro de esa función.

     ---Se eliminan al terminar la función."""



def mi_funcion():
    x = 10  # Variable local
    print(x)

mi_funcion()  # Output: 10
print(x)  
# NameError: name 'x' is not defined