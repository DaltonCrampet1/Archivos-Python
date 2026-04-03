import random
letras = input("Ingrese Letras: ")
numeros = int(input("Ingrese Numeros: "))
simbolos = input("Ingrese Simbolos: ")
contrasena = ""
correcto = True
i = 0
abcdario = "abcdefghijklmnopqrstwxyz"
if len(letras) < 8:
    correcto = False
if numeros < 1000:
    correcto = False
if len(simbolos) < 3:
    correcto = False
while i != len(simbolos[-1]):
    j = simbolos[i]
    if j == abcdario or j == abcdario.upper() or j == int:
        correcto = False
    i = i + 1
numeros = str(numeros)
if correcto is True:
    while len(contrasena) != 8:
        num = random.randint(1, 4)
        if random.randint(1, 2) == 1 and len(contrasena) != 8:
            contrasena = contrasena + numeros[num]
        letr = random.randint(1, len(letras[-1]))
        if random.randint(1, 2) == 1 and len(contrasena) != 8:
            contrasena = contrasena + letras[letr]
        simb = random.randint(1, len(simbolos[-1]))
        if random.randint(1, 2) == 1 and len(contrasena) != 8:
            contrasena = contrasena + simbolos[simb]
    print(contrasena)
else:
    print("")
