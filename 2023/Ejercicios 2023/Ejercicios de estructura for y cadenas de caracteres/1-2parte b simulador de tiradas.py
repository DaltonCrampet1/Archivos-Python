import random
i = 1
cara1 = 0
cara2 = 0
cara3 = 0
cara4 = 0
cara5 = 0
cara6 = 0
for i in range(30):
    dado1 = random.randint(1, 6)
    if dado1 == 1:
        cara1 = cara1 + 1
    if dado1 == 2:
        cara2 = cara2 + 1
    if dado1 == 3:
        cara3 = cara3 + 1
    if dado1 == 4:
        cara4 = cara4 + 1
    if dado1 == 5:
        cara5 = cara5 + 1
    if dado1 == 6:
        cara6 = cara6 + 1
print("La cara 1 salio ", cara1, "veces")
print("La cara 2 salio ", cara2, "veces")
print("La cara 3 salio ", cara3, "veces")
print("La cara 4 salio ", cara4, "veces")
print("La cara 5 salio ", cara5, "veces")
print("La cara 6 salio ", cara6, "veces")
