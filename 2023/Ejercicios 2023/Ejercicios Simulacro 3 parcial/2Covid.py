lista = [{"casos": 3452, "muertos": 45},
         {"casos": 2269, "muertos": 53},
         {"casos": 2318, "muertos": 54},
         {"casos": 1278, "muertos": 33},
         {"casos": 2385, "muertos": 41},
         {"casos": 1185, "muertos": 31}]
i = 0
sumamuertos = 0
for i in range(len(lista)):
    sumamuertos = sumamuertos + lista[i]["muertos"]
promediomuertos = sumamuertos / len(lista)
print("Promedio de muertos =", promediomuertos)
n = int(input("Escriba el numero de n: "))
i = 0
sumacasos = 0
for i in range(n):
    sumacasos = sumacasos + lista[i]["casos"]
promediocasos = sumacasos / len(lista)
print("Promedio de casos en", n, "dias =", int(promediocasos))
