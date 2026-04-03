def Inserte_notas(a):
    for i in range(5):
        correcto = False
        while correcto is False:
            num = int(input("Inserte un numero del 1 al 10: "))
            if 0 < num < 11:
                correcto = True
                a += [num]
            else:
                print("Tiene que ser un numero del 1 al 10")
    return a


notas = []
Inserte_notas(notas)
notas.sort()
print("Menor:", notas[0], "Mediano:", notas[2], "Mayor:", notas[4])
