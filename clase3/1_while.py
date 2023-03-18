# 1. sentencia de la condicion
# 2. el ciclo

""" sintaxis
while condicion:
    # codigo a ejecutar
"""

count = 0

"""
while count <= 10:
    if count == 6:
        count += 1
        break
    print(count)
    count = count + 1
"""
"""
while count <= 10:

    if count == 6:
        count += 1
        # count=7
        continue # continuar con el siguiente ciclo

    print(count)
    count = count + 1
"""

count = 10  # valor inicial del contador

while count > 0:  # finaliza cuando count == 1
    print(count)
    count = count - 1  # count -= 1
