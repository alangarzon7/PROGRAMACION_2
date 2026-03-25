"""Calificación de un estudiante 
Según la nota del examen (de 0 a 100), asigná una letra: 
○ A: 90 o más 
○ B: entre 80 y 89 
○ C: entre 70 y 79 
○ D: entre 60 y 69 
○ F: menos de 60"""
print("====Programa de calificacion de notas====")
nota=int(input("Ingrese la nota deseada(0 a 100): ")) 
if nota>= 90 and nota <=100:
    print('La calificacion es "A" ')
elif nota>= 80 and nota <=89:
    print('La calificacion es "B" ')
elif nota>= 70 and nota <=79:
    print('La calificacion es "C" ')
elif nota>= 60 and nota <=69:
    print('La calificacion es "D" ')
else:
    print('La calificacion es "F" ')