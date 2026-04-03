def hexadecimal(letrita, letritas):
    i = 0
    while i != len(letrita[-1]):
        if letrita == "a":
            letrita = 10
        if letrita == "b":
            letrita = 11
        if letrita == "c":
            letrita = 12
        if letrita == "d":
            letrita = 13
        if letrita == "e":
            letrita = 14
        if letrita == "f":
            letrita = 15
        i = i + 1
        letritas = letritas + str(letrita)
    return letritas


def binarios(numerito, numeritos):
    i = 1
    while len(numerito[-1]) != i:
        numeritos = str(len(numerito[i])*2**len(numerito[i]))
        i = i + 1
    return numeritos


numero_inicial = str(input("Escriba su numero "))
numero_final = ""
binario = False
hexa = False
decimals = False
funciona = True
if numero_inicial[0] == "0":
    if numero_inicial[1] == "b":
        binario = True
    if numero_inicial[1] == "x":
        hexa = True
    else:
        if numero_inicial[2:] != int and numero_inicial[1] != "b":
            funciona = False
if funciona is True:
    if decimals is True:
        print(numero_inicial)
    if binario is True:
        binarios(numero_inicial[2:], numero_final)
        print(numero_final)
    if hexa is True:
        hexadecimal(len(numero_inicial[2:]), numero_final)
        print(numero_final)
else:
    print("-1")
