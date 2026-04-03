class personaje:
    def __init__(self, ubi1, ubi2, ubicacions, energia):
        correcto = True
        direcciones = ["norte", "sur", "este", "oeste"]
        while correcto is True:
            try:
                direccion = input("A donde se desea mover(norte, sur, este, oeste)?\n→")
                if direccion in direcciones:
                    correcto = False
                else:
                    print("Tiene que ser norte, sur, este, o oeste")
            except ValueError:
                print("Tiene que ser norte, sur, este, o oeste")
        correcto = True
        while correcto is True:
            try:
                casillero = int(input("Cuanto se desea mover?\n→"))
                correcto = False
            except ValueError:
                print("Tiene que ser un numero")
        if casillero <= self.energia:
            self.energia = self.energia - casillero
            if direccion == "norte":
                self.ubi1 = ubi1 + casillero
                self.ubicacions = [self.ubi1, self.ubi2]
                print("Ubicacion actual:", ubicacions, "\nEnergia actual:", energia)
            if direccion == "sur":
                self.ubi1 = ubi1 - casillero
                self.ubicacions = [self.ubi1, self.ubi2]
                print("Ubicacion actual:", ubicacions, "\nEnergia actual:", energia)
            if direccion == "oeste":
                self.ubi2 = ubi2 + casillero
                self.ubicacions = [self.ubi1, self.ubi2]
                print("Ubicacion actual:", ubicacions, "\nEnergia actual:", energia)
            if direccion == "este":
                self.ubi2 = ubi2 - casillero
                self.ubicacions = [self.ubi1, self.ubi2]
                print("Ubicacion actual:", ubicacions, "\nEnergia actual:", energia)
        else:
            print("No tienes suficiente energia\nUbicacion actual:", ubicacions, "\nEnergia actual:", energia)


ubi1s = 0
ubi2s = 0
ubicacionss = [ubi1s, ubi2s]
energias = 10
print("Ubicacion actual:", ubicacionss, "\nEnergia actual:", energias)
avanzo = True
while avanzo is True:
    quiereavanza = input("Quieres avanzar?\n→")
    if quiereavanza == "si":
        personaje(ubi1s, ubi2s, ubicacionss, energias)
    elif quiereavanza == "no":
        avanzo = False
    else:
        print("es (si o no)")
print("Ultima ubicacion en", ubicacionss)
print()
