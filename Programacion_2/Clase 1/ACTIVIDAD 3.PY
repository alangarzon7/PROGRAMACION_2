"""Actividad N° 3 🤓

1. Crear un diccionario que contenga nombre, edad
y carrera de un alumno y mostrar
el diccionario completo."""

alumno ={'Nombre':'Alan',
         'Edad': 25,
         'Carrera': 'Economia'
    
}
print(alumno)

#2. Utilizar el método get para mostrar el valor de la clave nombre.
print(alumno.get('Nombre'))

#3. Cambiar la edad del alumno y mostrar el diccionario completo.
alumno['Edad']=18
print(alumno)

#. Agrear un par clave valor que contenga el sexo del alumno. y mostrar
alumno['Sexo']='Masculino'
print(alumno)

#5. Usar el método pop() para remover la edad del alumno. Mostrar el diccionario completo.
alumno.pop('Edad')
print(alumno)


""" Crear un diccionario que contenga las notas de un alumno en
tres materias. Las materias son programación II, ciencia de datos,
programación I."""

notas={'Programacion II':8,
       'Ciencia de Datos': 9,
       'Programacion I': 7
    
}
print(notas.items())