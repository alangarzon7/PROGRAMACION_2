def contar_hasta_cero(n):
    if n <= 0:  
        # Caso base
        print("¡Boom!")
    else:  
        # Caso recursivo
        print(n)
        contar_hasta_cero(n - 1)  

contar_hasta_cero(5)

""" Advertencia!!!!!

→ Definir siempre un caso base para evitar bucles infinitos.

→ Asegurar que cada llamada recursiva progrese hacia el caso base.

La recursión consume más memoria y tiempo de ejecución que los 

bucles iterativos, por lo que debe utilizarse con cuidado."""