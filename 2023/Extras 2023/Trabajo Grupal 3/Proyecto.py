d = True
while d is True:
    try:
        numerito = int(input("ponele"))
        if numerito < 0:
            numerito = numerito/0
        else:
            print("caguabonga")
            d = False
    except ZeroDivisionError:
        print("AAA")
    except ValueError:
        print("Tiene que ser un numero")
