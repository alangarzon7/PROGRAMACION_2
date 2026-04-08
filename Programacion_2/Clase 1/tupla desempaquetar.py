"""Desempaquetar una tupla
Podemos extraer los elementos de una tupla en múltiples variables, este proceso se      
llama desempaquetar la tupla. Este proceso resulta útil  por múltiples motivos:

1. Trabajar con valores devueltos por funciones. Muchas funciones en Python devuelven múltiples valores
en forma de tupla. Si los necesitamos algunos de estos valores, podemos desempaquetarlos en variables 
separadas para trabajar con ellos.

2. Simplificar el código. Desempaquetar una tupla puede hacer que el código sea más limpio y fácil de
leer."""
# Una tupla de notas de un examen
notas = (9, 8, 7, 4, 5, 6)

# Queremos el primero, el segundo y "el resto" aparte
primero, segundo, *el_resto = notas

print(f"Ganador: {primero}")
print(f"Segundo puesto: {segundo}")
print(f"Demás notas: {el_resto}") 
# Resultado de el_resto: [7, 4, 5, 6] (se convierte en lista)

#otro ejemplo de la IA

numeros = (1, 2, 3, 4, 5, 100)

# Queremos el primero, el último y lo de adentro
inicio, *medio, fin = numeros

print(f"Inicio: {inicio}") # 1
print(f"Medio: {medio}")   # [2, 3, 4, 5]
print(f"Fin: {fin}")       # 100