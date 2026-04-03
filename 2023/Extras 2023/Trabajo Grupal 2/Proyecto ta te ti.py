FilaA = [" ", " ", " ", " ", ]
FilaB = [" ", " ", " ", " "]
FilaC = [" ", " ", " ", " "]
FilaD = [" ", " ", " ", " "]
JGanador = 3


def Ganando_por_horizontal(FILA, FICHITA):
    if FILA[0] == FICHITA and FILA[1] == FICHITA and FILA[2] == FICHITA:
        return True
    elif FILA[1] == FICHITA and FILA[2] == FICHITA and FILA[3] == FICHITA:
        return True


def Ganado_por_vertical(COLUMNA, FICHITA):
    if FilaA[COLUMNA] == FICHITA and FilaB[COLUMNA] == FICHITA and FilaC[COLUMNA] == FICHITA:
        return True
    elif FilaB[COLUMNA] == FICHITA and FilaC[COLUMNA] == FICHITA and FilaD[COLUMNA] == FICHITA:
        return True


def Ganador_por_diagonal(FILA1, FILA2, FILA3, X, FICHITA):
    if FILA1[X] == FICHITA and FILA3[X + 1] == FICHITA and FILA2[X - 1] == FICHITA:
        return True
    elif FILA1[X] == FICHITA and FILA3[X - 1] == FICHITA and FILA2[X + 1] == FICHITA:
        return True


J1 = input("Ingrese el nombre del jugador 1 ➢ ")
J2 = input("Ingrese el nombre del jugador 2 ➢ ")
gano1 = False
gano2 = False
lista2 = []
print("       __1___2___3___4__")
print(f"FILA A | {FilaA[0]} | {FilaA[1]} | {FilaA[2]} | {FilaA[3]} |")
print("       -----------------")
print(f"FILA B | {FilaB[0]} | {FilaB[1]} | {FilaB[2]} | {FilaB[3]} |")
print("       -----------------")
print(f"FILA C | {FilaC[0]} | {FilaC[1]} | {FilaC[2]} | {FilaC[3]} |")
print("       -----------------")
print(f"FILA D | {FilaD[0]} | {FilaD[1]} | {FilaD[2]} | {FilaD[3]} |")
print("       _________________")
listafila = ["A", "B", "C", "D"]
listacolumna = [1, 2, 3, 4]
for turnos in range(0, 16):
    if turnos % 2 != 0:
        correctu = False
        while correctu is False:
            correctu = True
            filacorrecta = False
            while filacorrecta is False:
                lista1 = []
                print(J1)
                Input_Fila_1 = str(input("ponga la fila que quiere marcar ➢ "))
                for i in range(4):
                    if Input_Fila_1 == listafila[i]:
                        filacorrecta = True
            Input_Fila_1.isupper()
            Input_Columna_1 = int(input("ponga la posicion ➢ ")) - 1
            for i in range(len(lista1)):
                lista2.append([Input_Fila_1][Input_Columna_1])
                if lista2 == lista1[i]:
                    correctu = False
                    print("Escriba una posicion que no este ya usada")
        lista1.append(lista2)
        if Input_Fila_1 == "A" and FilaA[Input_Columna_1] != "0":
            FilaA[Input_Columna_1] = "X"
        elif Input_Fila_1 == "B":
            FilaB[Input_Columna_1] = "X"
        elif Input_Fila_1 == "C":
            FilaC[Input_Columna_1] = "X"
        elif Input_Fila_1 == "D":
            FilaD[Input_Columna_1] = "X"
        HORIZONTAL = [Ganando_por_horizontal(FilaA, "X"), Ganando_por_horizontal(FilaB, "X"),
                      Ganando_por_horizontal(FilaC, "X"),
                      Ganando_por_horizontal(FilaD, "X")]
        VERTICAL = [Ganado_por_vertical(0, "X"),
                    Ganado_por_vertical(1, "X"),
                    Ganado_por_vertical(2, "X"),
                    Ganado_por_vertical(3, "X")]
        DIAGONAL = [Ganador_por_diagonal(FilaB, FilaA, FilaC, 1, "X"),
                    Ganador_por_diagonal(FilaB, FilaA, FilaC, 2, "X"),
                    Ganador_por_diagonal(FilaC, FilaB, FilaD, 1, "X"),
                    Ganador_por_diagonal(FilaC, FilaB, FilaD, 2, "X")
                    ]
        if True in HORIZONTAL or True in VERTICAL or True in DIAGONAL:
            gano1 = True
            break
        print("       __1___2___3___4__")
        print(f"FILA A | {FilaA[0]} | {FilaA[1]} | {FilaA[2]} | {FilaA[3]} |")
        print("       -----------------")
        print(f"FILA B | {FilaB[0]} | {FilaB[1]} | {FilaB[2]} | {FilaB[3]} |")
        print("       -----------------")
        print(f"FILA C | {FilaC[0]} | {FilaC[1]} | {FilaC[2]} | {FilaC[3]} |")
        print("       -----------------")
        print(f"FILA D | {FilaD[0]} | {FilaD[1]} | {FilaD[2]} | {FilaD[3]} |")
        print("       _________________")
    else:
        correctu = False
        while correctu is False:
            correctu = True
            filacorrecta = False
            while filacorrecta is False:
                lista1 = []
                print(J1)
                Input_Fila_2 = str(input("ponga la fila que quiere marcar ➢ "))
                for i in range(4):
                    if Input_Fila_2 == listafila[i]:
                        filacorrecta = True
            Input_Fila_2.isupper()
            Input_Columna_2 = int(input("ponga la posicion ➢ ")) - 1
            for i in range(len(lista1)):
                lista2.append([Input_Fila_2][Input_Columna_2])
                if lista2 == lista1[i]:
                    correctu = False
                    print("Escriba una posicion que no este ya usada")
        lista1.append(lista2)
        if Input_Fila_2 == "A":
            FilaA[Input_Columna_2] = "0"
        elif Input_Fila_2 == "B":
            FilaB[Input_Columna_2] = "0"
        elif Input_Fila_2 == "C":
            FilaC[Input_Columna_2] = "0"
        elif Input_Fila_2 == "D":
            FilaD[Input_Columna_2] = "0"
    print("       __1___2___3___4__")
    print(f"FILA A | {FilaA[0]} | {FilaA[1]} | {FilaA[2]} | {FilaA[3]} |")
    print("       -----------------")
    print(f"FILA B | {FilaB[0]} | {FilaB[1]} | {FilaB[2]} | {FilaB[3]} |")
    print("       -----------------")
    print(f"FILA C | {FilaC[0]} | {FilaC[1]} | {FilaC[2]} | {FilaC[3]} |")
    print("       -----------------")
    print(f"FILA D | {FilaD[0]} | {FilaD[1]} | {FilaD[2]} | {FilaD[3]} |")
    print("       _________________")
    HORIZONTAL2 = [Ganando_por_horizontal(FilaA, "0"), Ganando_por_horizontal(FilaB, "0"),
                   Ganando_por_horizontal(FilaC, "0"),
                   Ganando_por_horizontal(FilaD, "0")]
    VERTICAL2 = [Ganado_por_vertical(0, "0"),
                 Ganado_por_vertical(1, "0"),
                 Ganado_por_vertical(2, "0"),
                 Ganado_por_vertical(3, "0")]
    DIAGONAL2 = [Ganador_por_diagonal(FilaB, FilaA, FilaC, 1, "0"),
                 Ganador_por_diagonal(FilaB, FilaA, FilaC, 2, "0"),
                 Ganador_por_diagonal(FilaC, FilaB, FilaD, 1, "0"),
                 Ganador_por_diagonal(FilaC, FilaB, FilaD, 2, "0")
                 ]
    if True in HORIZONTAL2 or True in VERTICAL2 or True in DIAGONAL2:
        gano2 = True
        break
if gano1 is True:
    print("gano ", J2)
elif gano2 is True:
    print("gano ", J1)
else:
    print("empataron")
