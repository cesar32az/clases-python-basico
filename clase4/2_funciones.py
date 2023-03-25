# parametros opcionales
# 1 * 10  si no se pasa el segundo numero, por defecto va a tener el 2


def multiplador(num1, num2=2):
    print(num1 * num2)


multiplador(6, 10)
multiplador(4)


def asignar_salario(nombre_cuenta="default", salario=2000):
    print(f"la cuenta {nombre_cuenta}, tiene un salario de {salario}")


asignar_salario()


# Mejorando y comentando nuestro codigo
def sumar_numeros(num1: int, num2: int):
    """
    Funcion que recibe dos numeros y retorna la suma
    """

    return num1 + num2


sumar_numeros(23, 2346)
