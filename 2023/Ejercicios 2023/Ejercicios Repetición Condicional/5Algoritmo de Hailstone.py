numero = int(input("Escriba un numero: "))
while numero != 1:
    if numero % 2 != 0:
        numero = numero*3+1
    else:
        numero = numero/2
    print(numero)
print(numero)
