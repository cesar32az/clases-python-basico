# entorno global
var1 = "hola mundo"
print(var1)


def funcion1():
    # entorno 1
    name = "julio"
    var1 = "test funcion 1"


def funcion2():
    # entorno 2
    var1 = "test funcion 2"


var1 = "hola mundo 2"

funcion1()
funcion2()

print(var1)
