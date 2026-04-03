class Barco:
    def __init__(self, nombre, blindaje):
        self.nombre = nombre
        self.blindaje = blindaje
        self.status = 'N'

    def impacto(self):
        if self.blindaje > 0:
            self.blindaje -= 1
            self.status = 'T'
        else:
            self.status = 'H'
            print("ya esta hundido")

    def esta_hundido(self):
        pass

    def __str__(self):
        return f'{self.nombre} Tiene {self.blindaje} y su estado es {self.status}'
