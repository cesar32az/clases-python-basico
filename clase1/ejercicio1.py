# 1. Solicitar a un usuario cuanto saldo tiene (debera de estar en decimales)
# en base al saldo debera de imprimir si le alcanza o no a comprar el producto.
# Lista precio [150.5, 20.5, 80]

precios = [150.5, 20.5, 80]
saldo = float(input("Ingrese su dinero actual: "))
total = sum(precios)


""" if saldo >= total:
    print("Tiene el suficiente dinero para comprar los productos.")
else:
    print("No tiene el suficiente dinero para comprar los productos.")
 """
for precio in precios:
    if saldo >= precio:
        print(f"tu saldo es: {saldo} y el precio del producto es: {precio}")
        print("Tiene el suficiente dinero para comprar el producto.\n")
    else:
        print(f"tu saldo es: {saldo} y el precio del producto es: {precio}")
        print("No tiene el suficiente dinero para comprar el producto.\n")
