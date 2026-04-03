i = 1
i2 = 0
positivos = 0
negativos = 0
for i in range(6):
    numerito = int(input("Ingrese un numero entero "))
    if numerito < 0:
        negativos = negativos + numerito
    else:
        positivos = positivos + numerito
        i2 = i2 + 1
promedio = positivos/i2
print("sumatoria de negativos = ", negativos)
print("promedio de positivos = ", promedio)
