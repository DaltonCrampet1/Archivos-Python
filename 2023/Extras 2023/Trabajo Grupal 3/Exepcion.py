correcto = False
while correcto is False:
    try:
        Tablero = int(input("Ingrese la cantidad del tablero entre 3 y 10 ➢"))
        if 2 < Tablero < 11:
            correcto = True
        else:
            print("El numero tiene que ser entre 3 y 10")
    except ValueError:
        print("Tiene que ser un numero")
correcto = False
while correcto is False:
    try:
        dificultad = int(input("Ingrese la dificultad entre 1 y 3 ➢"))
        if 0 < dificultad < 4:
            correcto = True
        else:
            print("Tiene que ser un numero entre 1 y 3")
    except ValueError:
        print("Tine que ser un numero")

A = [""] * Tablero
print(A)

casillas = Tablero * Tablero
n_disparos = {1: 70, 2: 50, 3: 30}
disparos = (casillas * n_disparos[dificultad] / 100)
m_disparos = disparos - int(disparos)
if m_disparos > 0:
    disparos = int(disparos) + 1
else:
    disparos = int(disparos)
print("Disparos", disparos)

n_barcos = {
    3: {1: 1, 2: 1, 3: 1},
    4: {1: 2, 2: 1, 3: 1},
    5: {1: 2, 2: 2, 3: 1},
    6: {1: 3, 2: 2, 3: 1},
    7: {1: 4, 2: 2, 3: 1},
    8: {1: 4, 2: 3, 3: 1},
    9: {1: 5, 2: 3, 3: 1},
    10: {1: 6, 2: 3, 3: 1}
}

contador = 1
total_barcos = 0
for i in range(3):
    print(n_barcos[Tablero][contador])
    total_barcos = total_barcos + n_barcos[Tablero][contador]
    contador = contador + 1
