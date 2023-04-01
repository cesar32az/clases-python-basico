# Un diccionario es un tipo de dato en python
# tipo: dict
"""
diccionario = { "clave": "valor", .... }
diccionario['clave'] # para acceder a los valores
keys = llaves = claves
value = valores
"""

carro = {
    "color": "azul",
    "cantidad_ruedas": 4,
    "marca": "honda",
    "tamaño": "pequeño",
}

# print(f"mi carro es de color {carro['color']}")
# print(f"mi carro tiene {carro['cantidad_ruedas']} ruedas")
# print(f"mi carro es de marca {carro['marca']}")
# print(carro)


carro["modelo"] = "civic"

# print("nuevo diccionario: ", carro)

# moto = {}

# marca = input("ingrese la marca de la moto: ")
# modelo = input("ingrese el modelo de la moto: ")

# moto["marca"] = marca
# moto["modelo"] = modelo

# marca = input("ingrese la marca de la moto: ")
# modelo = input("ingrese el modelo de la moto: ")
# moto = {"marca": marca, "modelo": modelo}

moto = {"marca": "ducati", "modelo": "monster", "color": "azul"}

# for clave, valor in moto.items():
#     print(f"clave: {clave} - valor: {valor}")

# print(moto.get("color", "no especificado"))

print("claves:")
for clave in moto.keys():
    print(clave)

print("\nvalues:")
for value in moto.values():
    print(value)
