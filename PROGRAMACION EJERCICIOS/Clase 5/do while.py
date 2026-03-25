#El while primero hace una comparacion y luego ejecuta. El do while, por lo menos una vez se tiene que ejecutar una condicion
contador = 1
while True:
    print(f"Contador es {contador} ")
    contador +=1
    if contador > 5:
        break

#Diferencia con el WHILE
contador =1
while contador <5:
    print(contador)
    contador +=1
    