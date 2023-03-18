from operaciones import sumar, multiplicar, restar, dividir

# programa para obtener numeros y sumar o restar esos numeros

nombre = input("Ingrese su nombre: ")

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion a realizar: ")


print("hola ", nombre)

if operacion == "sumar":
    resultado = sumar(num1, num2)
    print(f"El resultado de la suma es: {resultado}")

if operacion == "multiplicar":
    resultado = multiplicar(num1, num2)
    print(f"El resultado de la multiplicacion es: {resultado}")

if operacion == "restar":
    resultado = restar(num1, num2)
    print(f"El resultado de la resta es: {resultado}")

if operacion == "dividir":
    resultado = dividir(num1, num2)
    print(f"El resultado de la division es: {resultado}")
