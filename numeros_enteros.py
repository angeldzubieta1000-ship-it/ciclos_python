#Numeros Enteros

a = int(input("Escriba un numero entero: "))

if a > 0:
    copiaNumero = a
    contadorCifras = 0
    sumaCifras = 0

    while copiaNumero > 0:
        cifra = copiaNumero % 10
        copiaNumero = copiaNumero // 10
        sumaCifras = sumaCifras + cifra
        contadorCifras = contadorCifras + 1

    print("El numero ingresado es:", a)
    print("Son:", contadorCifras)
    print("La sumatoria es:", sumaCifras)

else:
    print("No es un numero positivo"), a