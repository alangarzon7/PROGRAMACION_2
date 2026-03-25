"""Mostrá un menú simple: 
 1. Jugar 
 2. Ver puntuación 
 3. Salir 
El usuario debe ingresar una opción válida (1, 2 o 3). 
Si elige 3, el programa finaliza. 
Si ingresa otra opción, debe volver a preguntar. 
¿Cómo controlar el bucle con while y terminar con break?"""
print("===Bienvenido battlefield 6===")
print("Selecciona una opcion:")
print("1. Jugar")
print("2. Ver puntuacion")
print("3. Salir")
while True:
    opcion=int(input("Ingrese su opcion: "))
    if opcion==1:
        print("Carganto mapa. ¡Preparate para la batalla!")
    elif opcion==2:
        print("Estos son tus puntos")
    else:
        print("Saliendo el juego")
        break
    
    
    
    