numeros= range(1,11)
for num in numeros:
    if num % 2 ==0: #%saca el resto de una division por 2. SI el resto de la division es = 0 significa que va a ser par.
        continue  #Me va a saltear los numeros PARES.
    print(f"Numero impar: {num} ")  #ME va a mostrar los numeros IMPARES, por que los PARES los saltee.