votosAndroid = 0
votosiOS = 0

voto = input("Ingrese Android, iOS para votar: ")

while voto != "Fin":
    if voto == "Android":
        votosAndroid = votosAndroid + 1
    elif voto == "iOS":
        votosiOS = votosiOS + 1
    else:
        print("La opcion no es valida")

    voto = input("Ingrese Android, iOS para terminar: ")

if votosAndroid > votosiOS:
    print("Android gano")
elif votosAndroid < votosiOS:
    print("iOS gano")
else:
    print("Hay empate")