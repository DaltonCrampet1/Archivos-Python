palabra = input("Ingrese una palabra ")
cadena = ""
while palabra != "":
    cadena = cadena + ";" + palabra.strip()
    palabra = input("Ingrese una palabra ")
print(cadena[1:])
