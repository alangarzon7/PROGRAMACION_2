""" Sumar numeros hasta cero(while)
El usuario va ingresando numeros uno por uno. Cuando ingresa 0, el programa se detiene ty muestra la suma total.
¿que pasaria si el cero se pone al principio? ¿y si nunca se pone?"""
suma=0
numero=int(input("Porfravor ingresa un numero(0 para salir): "))
while numero != 0:
    suma=suma +numero
    print(suma)
    numero=int(input("Porfravor ingresa un numero(0 para salir): "))
    
print(f"La suma d elos numeros ingresados es: {suma}")  

#otra forma con while true
"""suma=0
while True:
    numero =  int(input("Porfravor ingresa un numero(0 para salir): "))
    suma = suma +numero
    if numero == 0:
        break

print(f"La suma d elos numeros ingresados es: {suma}")  
    """