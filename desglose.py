# Calcular el IVA - desglose.py

"""
    SIERRA CAMACHO AURORA
    GDS0151
    19/02/2020
"""

POR_IVA = 16

conteo_produc = 1
precio_total = 0

while conteo_produc <=5:
    mensaje = "Ingrecia el precio del producto {}: ".format(conteo_produc)
    
    precio_cadena = input(mensaje)

    precio = float(precio_cadena)

    precio_total = precio_total + precio

    conteo_produc = conteo_produc + 1

aumento = precio_total * (POR_IVA / 100)

precioIva = precio_total + aumento

print("Total: ${}".format(precio_total ))
print("IVA: {}".format(aumento))
print("Total con IVA: ${}".format(precioIva))



    

