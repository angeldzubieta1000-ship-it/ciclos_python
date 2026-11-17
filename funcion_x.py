while True:
    valorX = int(input("Ingrese el maximo valor para x: "))
    if valorX >= 0:
        break

for x in range(0, valorX + 1, 2):
    fun = x**3 + x**2 - 5
    print("Para x = ", x, " f(x) = ", fun)