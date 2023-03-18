# 1. rango para ejecutar nuestro ciclo

"""
for valor in rango:
    contenido de nuestro codigo
"""

"""# conteo de 1 a 5
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
"""
#         0    1    2
lista = ["a", "b", "c"]

# print(lista[2])

""" forma larga
for num in range(len(lista)):  # len(lista) == 3
    print(f"posicion: {num} valor: {lista[num]}")
"""
""" forma corta
for palabra in lista:
    print(palabra)
"""
"""

for num, palabra in enumerate(lista):
    print(f"posicion: {num} valor: {palabra}")
"""

# imprimir parejas de numeros menores que 3
# ( 0, 0 ) (0,1) (0,2) (1,0)
"""
for i in range(3):
    for j in range(3):
        print(f"i: {i} - j: {j}")
"""

nombres = ["carlos", "julio", "fernando", "brandon"]

frutas = ["manzana", "naranja", "fresa"]
"""
for nombre in nombres:
    for fruta in frutas:
        print(f"{nombre} se come una {fruta}")
"""

""" forma compleja
for i in range(len(nombres)):
    for j in range(len(frutas)):
        print(f"{nombres[i]} se come una {frutas[j]}")
"""

for num in range(1, 11):
    if not num % 2 == 0:
        print(num)
