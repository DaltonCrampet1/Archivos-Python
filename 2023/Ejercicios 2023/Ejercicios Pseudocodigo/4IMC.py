peso = int(input("Escriba su peso: "))
altura = int(input("Escriba su altura: "))
altura = altura**2
IMC = peso/altura
if IMC < 18.5:
    print("Bajo Peso")
if 18.5 <= IMC < 14.9:
    print("Peso adecuado")
if 25 <= IMC < 29.9:
    print("Sobrepeso")
if IMC >= 30:
    print("Obesidad")
