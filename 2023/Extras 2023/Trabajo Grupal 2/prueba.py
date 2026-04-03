lista = ["A", "B", "C"]
correcto = False
while correcto is False:
    correcto = True
    cosita = input("Inserte una letra ")
    for i in range(len(lista)):
        if cosita == lista[i]:
            print("A")
            correcto = False
print("B")
