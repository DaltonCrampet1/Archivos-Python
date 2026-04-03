listaicantidad = []
listagramos = []
listaingredientes = []
i = 0
while i != 1:
    try:
        cuantos = int(input("Ingrese cuantos ingredientes va a utilizar: "))
        i = 1
    except ValueError:
        print("Tiene que ser un numero")
i = 0
while i != cuantos:
    try:
        cantidades = int(input("Ingrese 3 cantidades: "))
        listaicantidad.append(cantidades)
        i = i + 1
    except ValueError:
        print("Tiene que ser un numero")
print(listaicantidad)
i = 0
while i != cuantos:
    try:
        gramos = input("Ingrese las unidades(g, ml, gramos): ")
        listagramos.append(gramos)
        i = i + 1
    except ValueError:
        print("Tiene que ser un numero")
i = 0
while i != cuantos:
    try:
        ingredientes = input("Ingrese los ingredientes: ")
        listaingredientes.append(ingredientes)
        i = i + 1
    except ValueError:
        print("Tiene que ser un numero")
receta = input("Escriba la receta: ")
i = 0
print("\nIngredientes:\n\t")
while i != cuantos:
    print(listaicantidad[i], listagramos[i], listaingredientes[i])
    i = i + 1
print("\nProcedimiento:\n\t", receta)
