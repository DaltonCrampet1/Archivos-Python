lista = []
lista2 = []
num = 0
i = 0
while num >= 0:
    num = int(input("Ingrese un numero "))
    lista += [num]
del lista[-1]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista2.append(lista[i])
print(lista2)
