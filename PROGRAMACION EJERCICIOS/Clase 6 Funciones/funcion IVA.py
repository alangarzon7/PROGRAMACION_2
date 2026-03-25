"""Crear una función que calcule el IVA de un producto y lo imprima con
la leyenda “El IVA correspondiente al (valor ingresado) es (resultado de la función)."""
def calcular_iva_del_producto(a: float):
    return a* .21

producto=float(input("Ingrese el valor de su producto para calcular el IVA: "))
iva= calcular_iva_del_producto(producto)

print(f"El IVA correspondiente a {producto}, es {iva}")
