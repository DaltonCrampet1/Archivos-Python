fecha = input("Ingrese su fecha en formato dd/mm/aaaa\n-> ")
anio = fecha[6:]
mes = fecha[3:5]
dia = fecha[:2]
print("Año", anio, ", Mes", mes, ",Dia", dia)
