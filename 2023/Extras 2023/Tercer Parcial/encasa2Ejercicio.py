class info_lentes:
    def __init__(self, modelo, polarizado, porcentaje):
        self.modelo = modelo
        self.polarizado = polarizado
        self.porcentaje = porcentaje

    def __str__(self):
        return f"los lentes {self.modelo} {self.polarizado} tienen polarizado, con {self.porcentaje}%"

    def obtenerclase(self):
        if 80 <= porcentaje <= 100:
            print("CLASE 0")
        if 44 <= porcentaje <= 79:
            print("CLASE 1")
        if 19 <= porcentaje <= 43:
            print("CLASE 2")
        if 9 <= porcentaje <= 18:
            print("CLASE 3")
        if 3 <= porcentaje <= 8:
            print("CLASE 4")


modelo = input("Ingrese el modelo: ")
polarizado = input("Es polarizado?: ")
correcto = False
porcentaje = 0
while correcto is False:
    try:
        porcentaje = int(input("Ingrese el porcentaje de transmitancia: "))
        correcto = True
    except ValueError:
        print("El porcentaje tiene que ser un numero")
lente = info_lentes(modelo, polarizado, porcentaje)
print(lente)
lente.obtenerclase()
