numero = int(input("Escriba el dia de la semana en numero aqui: "))
if numero <= 7:
    if numero == 1:
        print("Hoy comienza la semana. Animo!")
    if numero == 5:
        print("Ya casi termina!")
    if numero == 6 or numero == 7:
        print("Siiii! Fin de semana!")
    if 1 < numero < 5:
        print("Vamos que se puede!")
else:
    print("Numero no valido")
