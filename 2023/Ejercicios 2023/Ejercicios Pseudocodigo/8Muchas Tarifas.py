peso = int(input("Ingrese el peso: "))
if peso < 900:
    precio = 19.80
if 900 < peso < 5000:
    precio = 21.90
if 5000 <= peso < 20000:
    precio = 16.50
if 20000 <= peso < 40000:
    precio = 13.20
if 40000 <= peso:
    print("Cotizar carga")
else:
    print(peso*precio-peso/10*100+5)
