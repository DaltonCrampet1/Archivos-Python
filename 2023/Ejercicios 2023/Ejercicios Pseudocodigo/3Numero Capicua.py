numero = int(input("Ingrese un numero de 5 digitos: "))
a = int(numero/10000)
b = int(numero/1000-a*10)
c = int(numero/100-(a+b)*10)
d = int(numero/10-(a+b+c)*10)
e = int(numero/1-(a+b+c+d)*10)
if a == e and b == d:
    print("Es capicua")
else:
    print("No es capicua")
#No Funciona