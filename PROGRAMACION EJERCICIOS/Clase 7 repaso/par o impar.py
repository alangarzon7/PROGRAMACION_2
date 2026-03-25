"""Situación: Pedir un número al usuario y decir si es 
par o impar. """

numero=int(input("Ingrese un numero: "))
if numero %2==0:
    print("Es par")
else:
    print("El numero es impar")
    
    
#Prueba con while

"""numero=int(input("Ingrese un numero(0 para salir): "))
while numero != 0:
    if numero %2==0:
        print("Es par")
        numero=int(input("Ingrese un numero(0 para salir): "))
    else:
        print("El numero es impar")
        numero=int(input("Ingrese un numero(0 para salir): "))
print("Gracias por utilizar nuestro programa")"""