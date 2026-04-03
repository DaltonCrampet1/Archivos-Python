import random
import time


def stat_de_carta():
   ATK_carta = random.randint(1, 6)
   DEF_carta = random.randint(1, 6)
   return ATK_carta, DEF_carta


def mano_jugador():
   Carta1 = stat_de_carta()
   Carta2 = stat_de_carta()
   Carta3 = stat_de_carta()
   return Carta1, Carta2, Carta3


def cantidad_jugadores(a):
   J1 = mano_jugador()
   J2 = mano_jugador()
   J3 = mano_jugador()
   J4 = mano_jugador()
   todos_los_J = J1, J2, J3, J4
   return todos_los_J[0:a]


numero_jugadores = int(input("Ingrese el numero de jugadores: "))
time.sleep(1)
partida1 = cantidad_jugadores(numero_jugadores)
if 1 < numero_jugadores < 5:
   if numero_jugadores == 2:
        mano1 = str(partida1[0:1])
        mano2 = str(partida1[1:2])
        print(partida1)
        print(mano1[2:8])
        print(mano2[2:24])
