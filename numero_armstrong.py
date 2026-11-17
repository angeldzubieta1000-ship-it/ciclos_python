num = int(input("Ingrese un numero: "))

original = num
n = len(str(num))
suma = 0

while num > 0:
    digito = num % 10
    suma = suma + digito ** n
    num = num // 10

if suma == original:
    print(original, "es un numero Armstrong")
else:
    print(original, "no es un numero Armstrong")