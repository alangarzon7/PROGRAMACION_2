Contraseña_correcta="1234"
intentos_restantes=3
while intentos_restantes >0:
    entrada=input("Ingrese su contraseña: ")
    if entrada==Contraseña_correcta:
        print("Contraseña correcta. Acceso concedido")
        break
    else:
        intentos_restantes -=1
        print(f"Contraseña incorrecta. Te quedan {intentos_restantes} intentos")
if intentos_restantes == 0:
    print("Acceso denegado, agotaste todos los intentos")  
      