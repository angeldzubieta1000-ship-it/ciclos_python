cantidadEst = int(input("Ingresa la cantidad de estudiantes: "))

notaSuma = 0
contadorEst = 0
aprob = 0
reprob = 0

while contadorEst < cantidadEst:
    nota = float(input("valor de la nota: "))
    if nota >= 3.0:
        aprob = aprob + 1
    else:
        reprob = reprob + 1
    notaSuma = notaSuma + nota
    contadorEst = contadorEst + 1

if cantidadEst > 0:
    promedio = notaSuma / cantidadEst
    print(f"El promedio de notas es: {promedio:.2f}")

print(f"Cantidad de estudiantes: {cantidadEst}")
print(f"Aprobaron: {aprob}")
print(f"Reprobaron: {reprob}")