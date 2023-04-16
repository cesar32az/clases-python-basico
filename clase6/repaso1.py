# Diferencia entre funcion y procedimiento
"""
Una función es un bloque de código que realiza una tarea específica 
y devuelve un valor a quien la llama. La función puede recibir parámetros 
como entrada, realizar operaciones con esos parámetros y luego devolver 
un valor calculado. Por lo tanto, una función tiene una entrada, 
un procesamiento y una salida.

Un procedimiento, por otro lado, también es un bloque de 
código que realiza una tarea específica, pero no devuelve un 
valor a quien lo llama. El procedimiento también puede recibir 
parámetros de entrada, realizar operaciones con esos parámetros, 
pero no devuelve ningún valor calculado.

Por ejemplo, si tuviéramos que escribir un código que calcule el área de un rectángulo, 
podríamos utilizar una función que reciba la longitud y la altura como parámetros y 
devuelva el valor calculado del área. En cambio, si tuviéramos que imprimir el área 
de un rectángulo en la pantalla, podríamos utilizar un procedimiento que reciba 
la longitud y la altura como parámetros y simplemente imprima el valor calculado 
en la pantalla.

Entonces, en resumen, la diferencia principal entre una función y un procedimiento 
es que la función devuelve un valor calculado y el procedimiento no lo hace.
"""

# repaso de condiciones

## verificar el departamento del dpi

# dpi = input("ingrese su dpi: ")

# sac = "0301"
# guatemala = "0101"

# print(dpi[-4:])

# if len(dpi) != 13:
#     print("dpi invalido")
# elif dpi[-4:] == sac:
#     print("usted es de sacatepequez")
# elif dpi[-4:] == guatemala:
#     print("usted es de guatemala")
# else:
#     print("no se encontro su departamento")

# edad = int(input("ingresa tu edad: "))

# # operador ternario
# # proposito: es una forma de simplificar una condicion if else en una sola linea
# resultado = "es mayor de edad" if edad >= 18 else "es menor de edad"

# print(resultado)


# repaso de ciclos o bucles
lista_numeros = list(range(1, 100))

# print(lista_numeros)


def imprimir_numeros(lista):
    lista_numeros_alreves = sorted(lista, reverse=True)
    for num in lista_numeros_alreves:
        if num == 3 or num == 6:
            continue
        print(num)


# imprimir_numeros(lista_numeros)

# animales = ["caballo", "gato", "perro"]

# for animal in animales:
#     if animal == "caballo":
#         continue
#     print(animal)

## ciclo while

"""count = 0

while count < 4:
    print(f"count: {count}, condicion: {count < 4}")
    count += 1
print(f"count: {count}, condicion: {count < 4}")

"""
"""
1. sumar
2. restar
0. salir
"""

"""
def obtener_opcion():
    opcion = int(input("ingrese una opcion: "))
    return opcion


opcion = None

while opcion not in [0, 1, 2]:
    opcion = obtener_opcion()
    print("opcion invalida valida\n")

print("opcion valida")
"""
"""
import time

while True:
    print("hola")
    time.sleep(2)
"""

# repaso de funciones


def sumar(num1, num2):
    return num1 + num2


def imprimir():
    print("hola")


## orden en argumentos


def imprimir_nombre(first_name, last_name):
    print(f"nombre: {first_name} apellido: {last_name}")


# imprimir_nombre("julio", "rodriguez")

# imprimir_nombre(last_name="rodriguez", first_name="julio")


def division(divisor, dividendo):
    print(divisor / dividendo)


# division(dividendo=5, divisor=10)


## funciones anidadas


def ejecutar_programa():
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def imprimir_resultado(num1, num2):
        suma = sumar(num1, num2)
        resta = restar(num1, num2)

        print(f"suma: {suma}, resta = {resta}")

    num1 = 10
    num2 = 5

    imprimir_resultado(num1, num2)


# ejecutar_programa()


animales = ["gato", "perro", "pez", "tigre", "cabra"]


def primer_y_ultimo_elemento(animales):
    primer_elemento = animales[0]
    ultimo_elemento = animales[-1]

    return primer_elemento, ultimo_elemento


primero, ultimo = primer_y_ultimo_elemento(animales)

print(f"primero: {primero} - ultimo: {ultimo}")
