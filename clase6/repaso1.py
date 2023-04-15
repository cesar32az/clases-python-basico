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

animales = ["caballo", "gato", "perro"]

for animal in animales:
    if animal == "caballo":
        continue
    print(animal)
