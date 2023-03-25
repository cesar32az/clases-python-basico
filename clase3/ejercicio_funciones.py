# 1. Escribir una función que reciba una lista de números como argumento e
# imprima los números pares de la lista original.

# 2. crear una funcion que reciba dos palabras, returne True o False
# si las palabras son iguales o no
# ej. palabra1 = "hola" palabra2 = "hola" -> True
# ej2. palabra1 = "hola" palabra2 = "adios" -> False

numeros = [
    1,
    2,
    5,
    2,
    2,
    2,
    16,
]


def imprimir_pares(numeros):
    numeros_sin_repetir = list(set(numeros))
    for num in numeros_sin_repetir:
        if num % 2 == 0:
            print(f"el numero es: {num}")


palabras = ["hola", "hola", "buenas", "tardes"]

print(list(set(palabras)))
