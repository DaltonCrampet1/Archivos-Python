lista = []
num = 0


def algo(a, b):
    while a != -1:
        a = int(input("Ingrese un numero "))
        b += [a]


algo(num, lista)
lista.remove(-1)
print(max(lista))
print(min(lista))
