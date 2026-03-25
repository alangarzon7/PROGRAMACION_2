"""promedio de 3 numeros: solicita al usuario que ingrese tres numeros, luego calcula y muestra el promedio de esos 3"""
print("*-----Bienvenido al sistema de promedios---------------*")
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

promedio= (num1+num2+num3)/3
print(f"El promedio de los 3 numeros ingresados es: {promedio}")

#Si quiero que me redondee el resultado para que no quede 2.9867485...ej..
"""Deberia usar el comando round."""
"""  promedio= round(num1+num2+num3)/3  --->asi se redondea el resultado""" 
