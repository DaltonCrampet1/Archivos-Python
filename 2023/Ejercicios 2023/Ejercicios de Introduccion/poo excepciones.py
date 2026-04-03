salir = False
while not salir:
    try:
        x = int(input("Ingrese numero: "))
        print(">>>>>>>>>>>>>>", x)
        salir = True
    except ValueError:
        print("No es un numero")
    else:
        print("Todo bien")
    finally:
        print("Buenooooo...")
