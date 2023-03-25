# crear un funcion que verifique si la contraseña del usuario es correcta


def obtener_contrasena():
    """
    Funcion que obtendra la contrasena del usuario desde una base de datos
    """
    # ... codigo y mas codigo

    return "asd123"


def verificar_contrasena(contrasena_usuario, contrasena_verificada):
    if contrasena_usuario == contrasena_verificada:
        print("es la contraseña correcta")
    else:
        print("la contraseña es incorrecta")


# contrasena = input("ingrese su contraseña: ")

verificada = obtener_contrasena()

# verificar_contrasena(contrasena, verificada)


"""
El factorial de un numero con una funcion recursiva
n!

1! = n * (n-1) * (n-2).... * 1

5! = 6* 5 * 4 * 3 * 2 * 1
"""


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


5 * 4 * 3 * 2 * 1

resultado = factorial(6)
print(resultado)


# funciones anidadas
def principal():
    print("Bienvenido")
    nombre = input("ingresa tu nombre: ")

    def saludar(nombre):
        print(f"hola {nombre}")

    saludar(nombre)


"""
1. Crea una función que tome como entrada dos números y 
devuelva el mayor de los dos. Luego utiliza una estructura de
control de flujo para imprimir un mensaje que indique cuál de 
los dos números es el mayor.

2. Crea una función que tome como entrada un número y devuelva True si es par y False
si es impar. Luego utiliza una estructura de control de flujo para imprimir un 
mensaje que indique si el número es par o impar.

3. Crea una función que tome como entrada una lista de números y devuelva 
la suma de todos los números de la lista. Luego utiliza una estructura de 
control de flujo para imprimir un mensaje que indique cuál es la suma de los 
números de la lista.

4. Crea una función que tome como entrada una lista de números y devuelva una 
lista con los números pares de la lista original. Luego utiliza una estructura 
de control de flujo para imprimir un mensaje que indique cuáles son los números 
pares de la lista original.

5. Crea una función que tome como entrada un número y una lista de números,
y devuelva True si el número está en la lista y False si no lo está.
Luego utiliza una estructura de control de flujo para imprimir un mensaje que 
indique si el número está o no en la lista.
"""
