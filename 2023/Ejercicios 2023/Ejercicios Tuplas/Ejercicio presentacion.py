def sumat(lista_tuplas):
    largo = len(lista_tuplas)
    lst_aux = []
    posicion = 0
    for _ in range(largo):
        suma = 0
        for tupla in lista_tuplas:
            suma += tupla[posicion]
        lst_aux.append(suma)
    return tuple(lst_aux)


resultado = sumat([(1, 2, 3), (3, 4, 5), (5, 6, 7)])
print(type(resultado))
print(resultado)
