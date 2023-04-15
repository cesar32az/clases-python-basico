# limpiar pantalla de usuario
import os
import time


def obtener_nombre():
    name = input("ingrese su nombre: ")
    print(name)


def limpiar_pantalla():
    input("presione enter para limpiar la pantalla")
    os.system("clear")


obtener_nombre()

limpiar_pantalla()
