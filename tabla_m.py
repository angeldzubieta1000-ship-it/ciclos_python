tabla = int(input("Ingrese la tabla a repasar: "))

aciertos = 0
desaciertos = 0

if tabla >= 1 and tabla <= 20:
    for multi in range(1, 11):
        producto = multi * tabla
        resp = int(input(f"Ingrese el resultado de {tabla} X {multi}: "))
        if resp == producto:
            aciertos = aciertos + 1
            print("Felicitaciones")
        else:
            desaciertos = desaciertos + 1
            print("Incorrecto, el valor esperado es", producto)

    print("La cantidad de aciertos es:", aciertos)
    print("La cantidad de desaciertos es:", desaciertos)

    if aciertos <= 5:
        print("Insuficiente")
    elif aciertos == 6 or aciertos == 7:
        print("Aceptable")
    elif aciertos == 8 or aciertos == 9:
        print("Sobresaliente")
    else:
        print("Excelente")