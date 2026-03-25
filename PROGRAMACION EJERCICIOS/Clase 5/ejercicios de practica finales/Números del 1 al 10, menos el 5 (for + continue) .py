"""Usá un bucle for para mostrar los números del 1 al 10, excepto el 5. 
Usá continue para saltearlo. 
¿Qué pasaría si se usa break en lugar de continue? """
#Si se usara break en lugar de continue, se cortaria al llegar al 5 y no mostraria los numeros restantes

for i in range(1,10):
    if i==5:
        continue
    print(i)
