# 1. Solicitar a un usuario cuanto saldo tiene (debera de estar en decimales)
# en base al saldo debera de imprimir si le alcanza o no a comprar el producto.
# Lista precio [150.5, 20.5, 80]

precios = [150.5, 20.5, 80]
saldo = float(input("Ingrese su dinero actual: "))
total = sum(precios)


if saldo >= total:
    print("Tiene el suficiente dinero para comprar los productos.")
else:
    print("No tiene el suficiente dinero para comprar los productos.")

for precio in precios:
    if saldo >= precio:
        print(f"tu saldo es: {saldo} y el precio del producto es: {precio}")
        print("Tiene el suficiente dinero para comprar el producto.\n")
    else:
        print(f"tu saldo es: {saldo} y el precio del producto es: {precio}")
        print("No tiene el suficiente dinero para comprar el producto.\n")


# ejercicio 2

# 2. ingresar la edad de 2 personas y el nombre, como resultado imprimir los datos y mostrar si es mayor a la
# primera persona o no y el nombre junto a la edad

nombre1 = input("Ingrese el nombre de la primera persona: ")
edad1 = int(input("Ingrese la edad de la primera persona: "))

nombre2 = input("Ingrese el nombre de la segunda persona: ")
edad2 = int(input("Ingrese la edad de la segunda persona: "))

if edad1 > edad2:
    print(nombre1, "tiene", edad1, "y es mayor que", nombre2, "que tiene", edad2)
elif edad2 > edad1:
    print(nombre2, "tiene", edad2, "y es mayor que", nombre1, "que tiene", edad1)
else:
    print(
        f"{nombre1} posee {edad1} y {nombre2} posee {edad2} Las 2 personas tienen la misma edad."
    )
