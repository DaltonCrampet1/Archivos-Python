llegue = False
numero = int(input("Ingrese un numero igual o mayor a 1: "))
i = 1
factorial = 1
while numero + 1 != i:
    factorial = factorial * i
    i = i + 1
print("El factorial de ", numero, "es ", factorial)
