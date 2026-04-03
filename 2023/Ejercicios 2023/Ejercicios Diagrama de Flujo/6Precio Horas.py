horastrabajadas = int(input("Escriba las horas trabajadas: "))
precioxhora = int(input("Escriba el precio por hora: "))
if horastrabajadas > 40:
    precioxhora = precioxhora*2
print("total a pagar: ", horastrabajadas*precioxhora)
