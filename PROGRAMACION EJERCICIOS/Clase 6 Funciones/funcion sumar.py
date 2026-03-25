def sumar(a,b):   #dentro del parentesis hay parametros
    """Aca podemos poner los docstring, hay que RESPETAR EL IDENTADO porque puede interpretar la funcionq ue son instrucciones y no un comentario"""
    return a + b

num1=int(input("Ingrese primer numero: "))  #---> ahora le estoy pasando argumentos a los parametros."""
num2=int(input("Ingrese segundo numero: ")) #---> ahora son argumentos."""

resultado = sumar(num1,num2)

print(f"El resultado es: {resultado}")