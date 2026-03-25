i=0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    
#NO me muestra el 0. Porque i es menor que 5, se cumple la condicion, se incrementa y DESPUES se imprime.