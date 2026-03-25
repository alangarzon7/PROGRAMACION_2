"""Situación: Pedir la edad del usuario y mostrar: 
● "Acceso denegado" si es menor de 18 
● "Acceso permitido" si tiene 18 o más"""

edad=int(input("Ingrese su edad: "))
if edad<18:
    print("Acceso denegado")
elif edad>=18:
    print("Acceso permitido")