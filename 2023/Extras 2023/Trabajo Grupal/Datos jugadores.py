def ficha_ingreso_J1():
    print("-"*36)
    nombre_J1 = input("Escriba su nombre J1\n➢ ")
    apellido_J1 = input("Escriba su apellido J1\n➢ ")
    nikname_J1 = input("Escriba su Nikname J1\n➢ ")


def ficha_ingreso_J2():
    print("-" * 36)
    nombre_J2 = input("Escriba su nombre J2\n➢ ")
    apellido_J2 = input("Escriba su apellido J2\n➢ ")
    nikname_J2 = input("Escriba su Nikname J2\n➢ ")


def ficha_ingreso_J3():
    print("-" * 36)
    nombre_J3 = input("Escriba su nombre J3\n➢ ")
    apellido_J3 = input("Escriba su apellido J3\n➢ ")
    nikname_J3 = input("Escriba su Nikname J3\n➢ ")


def ficha_ingreso_J4():
    print("-" * 36)
    nombre_J4 = input("Escriba su nombre J4\n➢ ")
    apellido_J4 = input("Escriba su apellido J4\n➢ ")
    nikname_J4 = input("Escriba su Nikname J4\n➢ ")


numero_jugadores = int(input("Ingrese el numero de jugadores: "))
if 1 < numero_jugadores < 5:
    if numero_jugadores == 2:
        ficha_ingreso_J1()
        ficha_ingreso_J2()
    if numero_jugadores == 3:
        ficha_ingreso_J1()
        ficha_ingreso_J2()
        ficha_ingreso_J3()
    if numero_jugadores == 4:
        ficha_ingreso_J1()
        ficha_ingreso_J2()
        ficha_ingreso_J3()
        ficha_ingreso_J4()
else:
    print("Los jugadores tienen que ser del 2 al 4 ")

