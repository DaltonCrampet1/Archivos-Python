namo = int(input("Escriba el numero del año que nacio: "))
nmes = int(input("Escriba el numero del mes que nacio: "))
ndia = int(input("Escriba el numero del dia que nacio: "))
aamo = int(input("Escriba el numero del año que actual: "))
ames = int(input("Escriba el numero del mes que actual: "))
adia = int(input("Escriba el numero del dia que actual: "))
tamo = aamo-namo
tmes = nmes-ames
tdia = ndia-adia
if tmes > 0:
    tamo = tamo+1
if tmes == 0:
    if ndia >= adia:
        tamo = tamo+1
print("Tienes ", tamo, " años")
