lista = [1, 2, 3]
lista.append(4) #Agrega un 4
print(lista)

lista2 = [3, 4, 5]
lista += lista2
lista += ["a b c"]
lista += ["a b c"]
lista += ["a b c"]
lista[1] = 7
print(lista)

del lista[2]
lista.remove("a b c")
print(lista)
