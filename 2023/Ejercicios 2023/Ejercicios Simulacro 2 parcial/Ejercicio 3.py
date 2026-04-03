numero = int(input("Ingrese un numero: "))
base = int(input("Ingrese una base: "))
numerito = ""
if base == 2 or base == 16:
    if base == 16:
        cociente = numero % 16
        while cociente != 0:
            cociente = int(numero / 16)
            Resto = int(numero % 16)
            if Resto == 10:
                Resto = "A"
            if Resto == 11:
                Resto = "B"
            if Resto == 12:
                Resto = "C"
            if Resto == 13:
                Resto = "D"
            if Resto == 14:
                Resto = "E"
            if Resto == 15:
                Resto = "F"
            numerito = numerito + str(Resto)
            numero = cociente
    if base == 2:
        cociente = numero / 2
        while cociente != 0:
            cociente = int(numero/2)
            Resto = int(numero % 2)
            numerito = numerito + str(Resto)
            numero = cociente
    print(str(numerito[::-1]))
else:
    print("")
