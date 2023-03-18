"""
if condicion:
    codigo
"""
"""
x = 100
if not x < 10:
    print(x)
"""

edad = 30
""" forma 1
if edad >= 0 and edad <= 11:
    print("edad esta entre 0 y 11")
elif edad >= 12 and edad <= 23:
    print("edad esta entre 12 y 23")
else:
    print("edad es mayor que 23")

"""

# forma 2 mas eficiente
if edad >= 0 and edad <= 11:
    print("edad esta entre 0 y 11")

if edad >= 12 and edad <= 23:
    print("edad esta entre 12 y 23")

if edad > 23:
    print("edad es mayor que 23")
