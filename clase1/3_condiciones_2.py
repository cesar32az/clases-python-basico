lista_productos = ["manzana", "pera", "naranja", "banana", "kiwi"]

numero_elementos = len(lista_productos)

print("nuestra lista tiene: ", numero_elementos, " elementos")

print(f"nuestra lista tiene: {numero_elementos} elementos")

print(f"nuestra lista tiene: {len(lista_productos)} elementos")


list_x = [1, "hola", 2.5]
print(f"nuestra lista x tiene: {len(list_x)} elementos")

if len(list_x) == 3:
    print("nuestra lista tiene 3 elementos")

# condicion que nuestra lista tenga entre 2 y 4 elementos

lista_productos2 = ["jamon", "queso", "pan", "lechuga"]

if len(lista_productos2) >= 2 and len(lista_productos2) <= 4:
    print("la lista cumple la condicion")
else:
    print("La lista no cumple la condicion")
