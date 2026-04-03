def errordesbasicos():
    y = 2
    x = [5, 3, 11, 25, 100, "hola", 0]
    print(x)
    for i in range(len(x)):
        print("i =", i, "==>", end=" ")
        try:
            a = int(x[i+1])
            print(y/a)
        except ValueError:
            print("Error de Valor")
        except IndexError:
            print("Error de indice")
        except ZeroDivisionError:
            print("Division por cero")
#
errordesbasicos()
