"""Crear un procedimiento que reciba un número 
y muestre su tabla de multiplicar del 1 al 10. """
def mostrar_tabla(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")

#uso
num=int(input("Ingrese un numero para mostrar su tabla de multiplicar: "))
mostrar_tabla(num)      