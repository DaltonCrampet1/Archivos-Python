import random
num = 1
suma1 = 0
suma2 = 0
suma3 = 0
suma4 = 0
suma5 = 0
suma6 = 0
while num != 29:
    dado = random.randint(1, 6)
    if dado == 1:
        suma1 = suma1 + 1
    if dado == 2:
        suma2 = suma2 + 1
    if dado == 3:
        suma3 = suma3 + 1
    if dado == 4:
        suma4 = suma4 + 1
    if dado == 5:
        suma5 = suma5 + 1
    if dado == 6:
        suma6 = suma6 + 1
    num = num + 1
print("El 1 aparecio", suma1, "veces")
print("El 2 aparecio", suma2, "veces")
print("El 3 aparecio", suma3, "veces")
print("El 4 aparecio", suma4, "veces")
print("El 5 aparecio", suma5, "veces")
print("El 6 aparecio", suma6, "veces")
