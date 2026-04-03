import random
i = 1
total_dados = 0
for i in range(20):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total_dados = total_dados + dado1 + dado2
promedio = total_dados/20
print("El promedio es: ", promedio)
