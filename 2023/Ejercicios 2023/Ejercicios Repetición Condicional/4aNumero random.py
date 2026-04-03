import random
I = 1
suma1 = 0
suma2 = 0
while I != 19:
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma1 = suma1 + dado1
    suma2 = suma2 + dado2
    I = I + 1
promedio = (suma1 + suma2)/40
print(promedio)