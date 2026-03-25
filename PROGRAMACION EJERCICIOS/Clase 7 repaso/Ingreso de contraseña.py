"""Ingreso de contraseña 
Situación: El programa debe pedir al usuario que 
ingrese una contraseña. 
Solo se permite acceder si la contraseña ingresada es 
"python123". 
Si es incorrecta, debe pedirla nuevamente hasta que 
sea correcta. 
Al ingresar la correcta, mostrar "Acceso autorizado". """

contrasena = input("Ingrese la contraseña: ") 
while contrasena != "python123": 
    print("Contraseña incorrecta.") 
    contrasena = input("Ingrese la contraseña: ") 
print("Acceso autorizado.")

"""Con dowhile"""
"""while True:
    contrasena = input("Ingrese la contraseña: ")
    
    if contrasena == "python123":
        break  # Esto rompe el bucle y sale
    
    print("Contraseña incorrecta. Intente de nuevo.")

print("Acceso autorizado.")"""