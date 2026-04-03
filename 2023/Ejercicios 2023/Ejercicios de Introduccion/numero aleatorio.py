import random
parar = ""
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
num7 = 0
num8 = 0
num9 = 0
num10 = 0
while parar == "":
    num = random.randint(1, 10)
    print(num)
    parar = input("_")
    if num == 1:
        num1 = num1 + 1
    if num == 2:
        num2 = num2 + 1
    if num == 3:
        num3 = num3 + 1
    if num == 4:
        num4 = num4 + 1
    if num == 5:
        num5 = num5 + 1
    if num == 6:
        num6 = num6 + 1
    if num == 7:
        num7 = num7 + 1
    if num == 8:
        num8 = num8 + 1
    if num == 9:
        num9 = num9 + 1
    if num == 10:
        num10 = num10 + 1
print("1", num1)
print("2", num2)
print("3", num3)
print("4", num4)
print("5", num5)
print("6", num6)
print("7", num7)
print("8", num8)
print("9", num9)
print("10", num10)
