import random
lista = []
for i in range(10):
    num = random.randint(1, 10)
    lista += [num]
for i in range(10):
    print(lista[i], lista[i]**2, lista[i]**3)
