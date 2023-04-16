def main():
    anio = int(input("Ingrese un año: "))
    if anio < 1924:
        print("El año ingresado es anterior al ciclo sexagenario del zodíaco chino.")
        return
    resultado = ciclo_sexagenario_zodiaco_chino(anio)
    print(f"El año {anio} corresponde a: {resultado}")


def ciclo_sexagenario_zodiaco_chino(anio):
    animales = [
        "Rata",
        "Buey",
        "Tigre",
        "Conejo",
        "Dragón",
        "Serpiente",
        "Caballo",
        "Cabra",
        "Mono",
        "Gallo",
        "Perro",
        "Cerdo",
    ]
    elementos = ["Madera", "Fuego", "Tierra", "Metal", "Agua"]
    anio_inicial = 1924  # El ciclo sexagenario del zodiaco chino comenzó en 1924
    animal_inicial = 0
    elemento_inicial = 0

    # Calculamos la posición del año en el ciclo sexagenario.
    posicion_anio = (anio - anio_inicial) % 60
    print(f"Posición del año en el ciclo sexagenario: {posicion_anio+1}")

    # Calculamos la posición del animal y del elemento en el ciclo sexagenario.
    posicion_animal = (animal_inicial + posicion_anio) % 12
    print(f"{posicion_animal=}")

    posicion_elemento = (elemento_inicial + posicion_anio // 2) % 5
    print(f"{posicion_elemento=}")

    # Obtenemos el animal y el elemento correspondiente a la posición calculada.
    animal = animales[posicion_animal]
    elemento = elementos[posicion_elemento]

    # Devolvemos el resultado.
    return f"{animal} de {elemento}"


main()
