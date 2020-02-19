# Tablas de multiplicar

"""
    Sierra Camacho Aurora
    GDS0151
    19/02/2020
"""

def tablas(num):
    LIMITE = 15
    contador = 1

    while contador <= LIMITE:
        resultado = contador * num

        print("{} x {} = {}".format(num, contador, resultado))

        contador = contador + 1

tablas(15)
