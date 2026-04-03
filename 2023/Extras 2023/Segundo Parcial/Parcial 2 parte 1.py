def dia_anterior(dd, mm, aa):
    print(dd, "/", mm, "/", aa)


dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
bisiesto = False
anterior_mes = 30
ames = mes - 1
if anio/400 == 0 or (anio/100 != 0 and anio/4 == 0):
    bisiesto = True

if ames == 1 or ames == 3 or ames == 5 or ames == 7 or ames == 8 or ames == 10 or ames == 0:
    anterior_mes = 31
if ames == 2:
    anterior_mes = 28
if bisiesto is True:
    anterior_mes = 29
if ames == 0:
    anio = anio - 1

if dia == 1:
    dia = anterior_mes
    mes = mes - 1
else:
    dia = dia - 1
if mes == 0:
    mes = 12
dia_anterior(dia, mes, anio)
