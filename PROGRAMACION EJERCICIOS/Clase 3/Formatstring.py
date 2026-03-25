nombre="Alan"
edad= 21
#saludo="Hola "+nombre+"!!! como estas?"+edad+"años de edad"
#print(saludo)    
#En este caso me va a dar error porque la variable edad es tomada como un entero, y al concatenar con +, el + solo sirve para concatenar texto(string).
#una solucion a esto es transformar la variable edada a string.
#----+-+-+-+-+-+-+-+-+-+-+-++-++-+-+-+-+-+--++-++-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-++-+-+-+-+-+
#Tambien se puede usar formatstring
saludo=f"Hola {nombre}!!! como estas? {edad} años de edad"
print(saludo) 

