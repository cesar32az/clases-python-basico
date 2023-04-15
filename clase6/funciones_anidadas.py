# funcion sencilla
# def sumar(num1, num2):
#     return num1 + num2


# print(total)


def calcular_suma(num1, num2):
    def sumar():
        return num1 + num2

    def imprimir_resultado():
        total = sumar()
        print(f"el resultado de la suma es: {total}")

    imprimir_resultado()

    return sumar()


# total = calcular_suma(2, 3)


def calcular_edad(anio):
    def calcular_edad_actual():
        return 2023 - anio

    def imprimir_edad():
        edad = calcular_edad_actual()
        print(f"Funcion interna: tu edad es: {edad}")

    imprimir_edad()

    return calcular_edad_actual()


edad = calcular_edad(1996)
