# metodos de textos

texto1 = "hola buenas tardes tardes tardes"
texto2 = "BUENAS TARDES"

texto1.upper()  # texto a mayusculas
texto1.lower()  # texto a minusculas
texto1.capitalize()  # inicio del texto en mayuscula

# print(texto2.upper())
# print(nombre.upper())

# split => ["julio", "rodriguez", "hola", "buenas"]

lista_texto1 = texto1.split()
# print(lista_texto1)

# print(texto1.replace("tardes", "noches"))

# metodos de numeros

num1 = 4
num2 = 235

# print(num2.bit_count())

# sume los numeros pares de la siguiente lista, lo realice con dos funciones distintas
numeros = [12, 23, 5, 346, 856, 2, 34]


def obtener_pares(numeros):
    numeros_pares = []
    for num in numeros:
        if num % 2 == 0:
            numeros_pares.append(num)
    return numeros_pares


def sumar_numeros(numeros):
    return sum(numeros)


numeros_pares = obtener_pares(numeros)

total = sumar_numeros(numeros_pares)

print(total)

palabras = ["hola", "julio"]

palabras.append("como")
palabras.append("estas?")

print(palabras)

print(" ".join(palabras))
