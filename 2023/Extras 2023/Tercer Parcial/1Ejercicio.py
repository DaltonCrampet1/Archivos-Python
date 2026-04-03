Joyas = {
    'Oro Rosa': {'Oro': 75, 'Cobre': 25},
    'Oro Blanco': {'Oro': 75, 'Paladio': 25},
    'Oro Amarillo': {'Oro': 100},
    'Platino Puro': {'Platino': 100},
    'Platino Iridio': {'Platino': 90, 'Iridio': 10},
    'Plata Pura': {'Plata': 100},
    'Paladio Platino': {'Paladio': 60, 'Platino': 40}
}
cadena = input("Ingrese las piezas con sus gramos: ")
# cadena = "Oro Rosa:10,Plata Pura:4,Oro Blanco:10"
cadena = (cadena.split(","))
largo = len(cadena)

Oro = 0
Cobre = 0
Paladio = 0
Platino = 0
Iridio = 0
Plata = 0

for i in range(largo):
    elementos = cadena[i].split(":")
    material = str(elementos[0])
    gramos = int(elementos[1])
    if "Oro" in Joyas[material]:
        Oro = Oro + gramos * Joyas[material]["Oro"] / 100
    if "Cobre" in Joyas[material]:
        Cobre = Cobre + gramos * Joyas[material]["Cobre"] / 100
    if "Paladio" in Joyas[material]:
        Paladio = Paladio + gramos * Joyas[material]["Paladio"] / 100
    if "Platino" in Joyas[material]:
        Platino = Platino + gramos * Joyas[material]["Platino"] / 100
    if "Iridio" in Joyas[material]:
        Iridio = Iridio + gramos * Joyas[material]["Iridio"] / 100
    if "Plata" in Joyas[material]:
        Plata = Plata + gramos * Joyas[material]["Plata"] / 100
print(f"Nesecisas: Oro: {Oro}, Cobre: {Cobre}, Paladio: {Paladio}, Platino: {Platino}, Iridio: {Iridio}, Plata: "
      f"{Plata}")
