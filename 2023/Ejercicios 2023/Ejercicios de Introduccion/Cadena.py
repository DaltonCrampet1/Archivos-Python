palabra = "Uruguay"
if "a" in palabra:
    print("La letra a esta en la palabra", palabra, "\n")
if "n" not in palabra:
    print("La letra n no esta en la palabra", palabra, "\n")
for letrita in palabra:
    print(letrita)
vocales = "AEIOUaeiou"
palabra_sin_vocales = ""
palabra_sin_vocales2 = ""
if letrita not in vocales:
    palabra_sin_vocales = palabra_sin_vocales + letrita
print(palabra_sin_vocales, "\n")
for i in range(len(palabra)):
    if palabra[i] not in vocales:
        palabra_sin_vocales2 = palabra[i]
for i in range(2, len(palabra)):
    print(palabra[i])
for i in range(2, len(palabra, 2)):
    print(palabra[i])
