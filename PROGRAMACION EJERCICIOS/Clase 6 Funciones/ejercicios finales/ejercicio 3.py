"""3. Obtener iniciales de un nombre completo""" 
def obtener_iniciales(nombre, apellido): 
 return nombre[0].upper() + apellido[0].upper() 
iniciales = obtener_iniciales("juan", "perez") 
print(iniciales)