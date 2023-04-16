def main():
    capital = float(input("Ingrese el capital: "))
    interes = float(input("Ingrese el interes: "))

    def anios_para_duplicar(capital, tasa):
        anios = 0
        doble_capital = capital * 2
        while capital <= doble_capital:
            capital += capital * (tasa / 100)
            anios += 1
            print(f"Capital: {capital}. Tasa: {tasa}%. Años: {anios}")
        return anios

    anios = anios_para_duplicar(capital, interes)

    print(f"C: {capital}. R: {interes}%. Años: {anios}")


main()
