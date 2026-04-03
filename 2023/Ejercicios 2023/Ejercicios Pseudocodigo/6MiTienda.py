peso = int(input("Ingrese el peso: "))
tarifa = 21.99
if peso < 3:
    print("Total a pagar: ", peso*tarifa)
if 3 < peso < 5:
    peso = peso-peso*30/100
    print("Total a pagar: ", peso*tarifa)
if peso > 5:
    peso = peso-peso*50/100
    print("Total a pagar: ", peso*tarifa)
