"""Verificacion de edad para ver una pelocula-
Supongamos que estas desarrollanmdo un programa para el cine y deseas asegurarte que los
espectadores sean lo suficientemente mayores
debes solicitar la edad del espectador y permitir ela cceso solo si tiene al menos 13 años"""

print("======Bienvenido al CineCinemas 4=======")
print("Recordatorio: Solo peliculas aptas para mayores de 13 años")

edad=int(input("Ingrese su edad: "))
if edad>=13 and edad<= 100:
    print("Ustded es mayor puede ver las peliculas")
else:
    print("Usted no puede ver las peliculas, es menor de 13 años")

