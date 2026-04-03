tiempo = input("Ingrese la hora en formato hh:mm:ss ")
hora = int(tiempo[0:2])
minuto = int(tiempo[3:5])
segundos = int(tiempo[6:])
apm = "am"
if hora > 12:
    hora = hora - 12
    apm = "pm"
print("Hora:", hora, apm, ", Minutos:", minuto, ", Segundos:", segundos)
