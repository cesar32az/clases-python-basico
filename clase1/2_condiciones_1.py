# validar si me alcanza el saldo para comprar un producto

# el precio del producto debe ser menor a 3200.50

saldo_actual = 3200.50

precio_producto = float(input("Ingrese el precio del producto: "))

es_menor = precio_producto <= saldo_actual

if es_menor:
    print("Tienes saldo suficiente para comprar el producto")
else:
    print("No tienes saldo suficiente para comprar el producto")
