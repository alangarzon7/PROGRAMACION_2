""" Ingresar una nota del 0 al 10 y mostrar si 
el estudiante está: 
● Desaprobado (0 a 5) 
● Aprobado (6 a 8) 
● Sobresaliente (9 o 10) """

nota=int(input("Ingrese la nota del alumno(del 0 al 10)"))
if nota >=0 and nota <= 5:
    print(f"Su nota es {nota}, esta desaprobado")
elif nota >=6 and nota<=8:
    print(f"Alumno aprobado con {nota}")
elif nota >=9 and nota <=10:
    print(f"Alumno sobresaliente, aprobo con un {nota}")
else:
    print("Nota invalida")
