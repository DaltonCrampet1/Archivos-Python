numero = int(input("Escriba el año: "))
if numero % 400 == 0:
    print("Bisiesto")
elif numero % 4 == 0 and numero % 100 != 0:
    print("Bisiesto")
else:
    print("No es Bisiesto")
