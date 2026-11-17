while True:
    cantidadNumeros = int(input("Ingrese la cantidad de numeros: "))
    if cantidadNumeros >= 0:
        break

for num in range(1, cantidadNumeros + 1):
    print(num, num * num, num + num * num)