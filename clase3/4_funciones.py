"""
Funcion: bloque de codigo con una tarea especifica

# definimos la funcion
def nombre_funcion(parameto1, parametro2...):
    codigo

# ejecutar funcion
nombre_funcion(argumento)
"""

# funcion que no devuelve valor y no tiene parametros
"""def saludar():
    print("Hola mundo!")

saludar()
"""
"""
# funcion que no devuelve valor, pero que si tiene parametros
def comer(comida, bebida):
    print(f"voy a comer {comida}")
    print(f"voy a tomar {bebida}")


comer("hamburguesa", "cocacola")  # llamamos nuestra funcion
"""

# funcion que devuelva un valor, sin parametros

"""
def obtener_mes():
    mes = "enero"

    return mes


valor = obtener_mes()

print(valor)
"""
"""
# funcion que devuelve valor y recibe parametros
def obtener_nombre(posicion):
    nombres = ["julio", "carlos", "fernando", "cesar", "asdf", "sgds"]

    if posicion > len(nombres) - 1:
        print("el numero no puede ser mayor que 2")
        return

    nombre = nombres[posicion]

    return nombre


valor = obtener_nombre(5)

if valor:
    print(valor)
"""

"""num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))


def sumar(a, b):
    suma = a + b
    return suma


def resta(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


valor = sumar(num1, num2)
print("la suma es ", valor)

valor2 = resta(num1, num2)
print("la resta es ", valor2)

valor4 = resta(num2, num1)
print("la segunda resta es ", valor4)

valor3 = multiplicar(num1, num2)
print("la multiplicacion es ", valor3)
"""
"""
nombres = ["julio", "cesar", "carlos", "francisco"]


def saludar(nombre):
    print(f"hola {nombre}, es un gusto saludarte")


for nombre in nombres:
    saludar(nombre)
"""

""" forma larga
def sumar_precios(lista_precios):
    total = 0
    for precio in lista_precios:
        total += precio
    return total
"""


def sumar_precios(lista_precios):
    return sum(lista_precios)


total = sumar_precios([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(sorted(["b", "x", "y", "a"]))

print(sorted([6, 1, 78, 2, 3, 8], reverse=False))
