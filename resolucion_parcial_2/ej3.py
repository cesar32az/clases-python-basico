def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    opcion = input(
        """
        Selecciona una opción:

        Menu:
        1. Menor
        2. Mayor
        3. Media
        4. Primo
        5. MCD
        0. Salir

    opcion: """
    )
    match opcion:
        case "1":
            print(f"El menor es: {calcular_menor(num1, num2)}")
        case "2":
            print(f"El mayor es: {calcular_mayor(num1, num2)}")
        case "3":
            print(f"La media es: {calcular_media(num1, num2)}")
        case "4":
            print(f"El número {num1} {verificar_primo(num1)}")
            print(f"El número {num2} {verificar_primo(num2)}")
        case "5":
            print(f"El MCD es: {calcular_mcd(num1, num2)}")
        case "0":
            print("Adios...")
        case _:
            print("Opción inválida")


def calcular_menor(num1, num2):
    return num1 if num1 < num2 else num2  # Operador ternario


def calcular_mayor(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


def calcular_media(num1, num2):
    return (num1 + num2) / 2


def verificar_primo(num):
    for n in range(2, num):
        print(f"num: {num} % n: {n} = {num % n}")
        if num % n == 0:
            return "no es primo"
    return "es primo"


"""
modulo %
2 / 2 = 1.0 % -> 0
5 / 2 = 2.5 % -> 1
"""
"""
range(2, 7) -> 2, 3, 4, 5, 6
5 ->  2, 3, 4
7 ->  2, 3, 4, 5, 6
8 ->  2, 3, 4, 5, 6, 7 # no es primo
"""


def calcular_mcd(num1, num2):
    print(f"num1: {num1} num2: {num2}")
    if num2 == 0:
        return num1
    return calcular_mcd(num2, num1 % num2)


# https://es.symbolab.com/solver/gcf-calculator/mcd%20%2018%2C24?or=input

main()
