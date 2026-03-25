"""Situación: El programa debe simular un menú bancario 
simple. 
Mostrar el siguiente menú al usuario: 
1. Ver saldo   
2. Realizar transferencia   
3. Salir 
El usuario debe ingresar un número del 1 al 3 según la opción 
que quiera. El programa mostrará un mensaje correspondiente: 
● Si elige 1 → mostrar "Su saldo es $15.000" 
● Si elige 2 → mostrar "Transferencia realizada con éxito" 
● Si elige 3 → mostrar "Saliendo del sistema..." 
● Si elige otro número → mostrar "Opción inválida"""

print("====Bienvenido a nuestra sucursal bancaria====")

while True:
    print("Menu de opciones.")
    print("1.Ver saldo")
    print("2.Realizar transferencia")
    print("3.Salir")
                   
    opcion=int(input("Elija una opcion: "))
    
    if opcion==1:
        print("Su saldo es de $15.000")
    elif opcion ==2:
        print("Su transferencia fue realizada con exito")
    elif opcion==3:
        print("Saliendo el sistema")
        break
    else:
        print("Opcion invalida.")
        
print("Gracias por utilizar nuestro sistema bancario")