lista1 = []
lista2 = []
removedor = []
num = 1
while num != 0:
    num = int(input("Ingrese un numero, para detenerse ingrese 0 ➢ "))
    lista1 += [num]
del lista1[-1]
i = 1
lista1.sort()
lista2.append(lista1[0])
print(lista1)
for i in range(len(lista1)):
    lista2.append(lista1[i])
    if lista2[-2] == lista2[-1]:
        del lista2[-1]
print(lista2)
