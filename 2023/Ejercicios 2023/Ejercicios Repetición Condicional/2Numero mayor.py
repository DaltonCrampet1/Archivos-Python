numero = int(input("Escriba un numero: "))
mayor = 0
while numero != 0:
    if mayor < numero:
        mayor = numero
    numero = int(input("Escriba un numero: "))
print("El mayor es: ", mayor)
