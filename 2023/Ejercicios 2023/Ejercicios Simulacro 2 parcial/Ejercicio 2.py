import random
num = int(input("Escriba el numero de digitos para su contraseña: "))
i = 0
contrasena = ""
while i in range(num):
    numerito = random.randint(1, 9)
    contrasena = contrasena + str(numerito)
    i = i + 1
print("Su contraseña es: ", contrasena)
