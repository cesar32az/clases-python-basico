from math import sqrt


def calcular_hipotenusa(a, b):
    a_cuadrado = calcular_cuadrado(a)
    b_cuadrado = calcular_cuadrado(b)

    suma = sumar(a_cuadrado, b_cuadrado)

    resultado = calcular_raiz(suma)

    return resultado


def calcular_cuadrado(num):
    return num**2


def sumar(num1, num2):
    return num1 + num2


def calcular_raiz(num):
    return sqrt(num)


valor = calcular_hipotenusa(2, 4)

print(f"la hiponetusa de 2 y 4 es: {valor}")
