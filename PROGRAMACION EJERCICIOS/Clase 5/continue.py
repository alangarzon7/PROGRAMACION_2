#se utiliza dentro de bulces como for y while
#continue omite el resto del codifo dentro de la iteracion actual del bucle y pasa a la siguiente iteracion.
#ejemplo. si encuentra el 3, en vez de frenar el codigom lo saltea al 4, yno muestra el 3.
for letra in "Python":
    if letra == "t":
        continue #Si letra ==t continua.., no la muestra
    print(letra)
    