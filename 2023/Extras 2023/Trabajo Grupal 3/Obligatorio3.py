from Obligatorio3Parte2 import Barco
import random

correcto = False
abcdario = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

buques = {1: Barco('buquesito', 1), 2: Barco('buque', 2), 3: Barco('buquetazo', 3)}
while correcto is False:
    try:
        Casillas = int(input("Ingrese la cantidad del tablero entre 3 y 10 ➢"))
        if 2 < Casillas < 11:
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
    filas = []
    Tablero = []
    for x in range(0, Casillas):
        Tablero.append([])
        for i in range(0, Casillas):
            Tablero[x].append("")

Total_casillas = Casillas * Casillas
n_disparos = {1: 70, 2: 50, 3: 30}
disparos = (Total_casillas * n_disparos[dificultad] / 100)
m_disparos = disparos - int(disparos)
if m_disparos > 0:
    disparos = int(disparos) + 1
else:
    disparos = int(disparos)

print(Tablero)
Tablero_visible = []
for o in range(0, Casillas):
    Tablero_visible.append([])
    for i in range(0, Casillas):
        Tablero_visible[o].append("")


def planteo_de_barcos(Cantidad, resistencia):
    es_vacio = ""
    for z in range(0, Cantidad):
        for _ in range(0, 2):
            x = random.randint(0, Casillas - 1)
            y = random.randint(0, Casillas - 1)
            while Tablero[x][y] != es_vacio:
                x = random.randint(0, Casillas - 1)
                y = random.randint(0, Casillas - 1)

            Tablero[x][y] = "a"

        for o in Tablero:
            for i in o:
                if i == "a":
                    Tablero_visible[Tablero.index(o)][o.index(i)] = "i"
        for o in Tablero:
            for i in range(0, Casillas):
                if o[i] == "a":
                    o[i] = buques[resistencia]
                    o[i].nombre += str(z)


letras_Tablero = list(abcdario.keys())

for letras in range(Casillas):
    print(f" | {letras_Tablero[letras]}", end=" |")
print("\n")
for o in range(0, Casillas):
    print(f'{o}')
    for i in range(0, Casillas):
        print(f"  | {Tablero_visible[o][i]}", end=" |")
    print()
Barcos_Totales = Casillas
planteo_de_barcos(2, 1)
fin = False
while fin is False:
    Piu_Piu = str(input("entra unas coordenadas ➢"))
    try:
        if "" not in Tablero[abcdario[Piu_Piu[0]]][int(Piu_Piu[1])]:
            print("le diste")
            disparos = disparos - 1
            Barcos_Totales = Barcos_Totales - 1
        else:
            print("no")
            print(Piu_Piu)
            disparos = disparos - 1
    except TypeError:
        print("le diste")
        Tablero[abcdario[Piu_Piu[0]]][int(Piu_Piu[1])].impacto()
        print(Tablero[abcdario[Piu_Piu[0]]][int(Piu_Piu[1])].blindaje)
    except KeyError:
        print("Esa no es una coordenada valida")
    except IndexError:
        print("Esa no es una coordenada valida")
    if disparos == 0:
        print("Gano el Programa")
        fin = True
    if Barcos_Totales == 0:
        print("Gano el Jugador")
        fin = True
