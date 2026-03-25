"""El programa genera un numero secreto entre el 1 y el 10. El usuario tiene intentos ilimitados para adivinarlo.
Si aceerta, el prgrama muestra un mensaje y termina con un break.
Sino vuelve a pedir.
¿cOMO EVITAR QUE EL PROGRAMA NUNCA TERMIE SI EL USUARIO SE EQUIVOCA SIEMPRE?
"""
numero_secreto= 5

while True:
    intento=int(input("Adivina el numero del 1 al 10: "))
    if numero_secreto == intento:
        print("Adivinaste!!!")
        break
    else:
      print("Numero incorrecto, intenta otra vez.")
    