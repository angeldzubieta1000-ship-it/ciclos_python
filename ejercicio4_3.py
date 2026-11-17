num = int(input("Escriba un numero entero: "))

if num > 0:
    copiaNumero = num
    contadorCifra = 0
    sumaCifra = 0

    while copiaNumero > 0:
        cifra = copiaNumero % 10
        copiaNumero = copiaNumero // 10
        sumaCifra = sumaCifra + cifra
        contadorCifra = contadorCifra + 1

    print("La cantidad de cifras del numero", num, "es", contadorCifra)
    print("La sumatoria de las cifras es", sumaCifra)
else:
    print("No es un numero positivo")