animales_frecuencias = [
 ('El Perro', (40, 60000)),
 ('El Gato', (48, 85000)),
 ('El Elefante', (16, 12000)),
 ('El Murciélago', (1000, 110000)),
 ('El Delfín', (75, 150000)),
 ('La Ballena', (10, 20000)),
 ('La Serpiente', (80, 600)),
 ('El Búho', (200, 12000)),
 ('La Rana', (100, 3000)),
 ('El Pez', (50, 1500))
]
Tormenta_eléctrica = 30
Grillos_en_la_noche = 400
Zumbido_en_colmena_de_abejas = 22000
tormenta = []
grillo = []
zumbido = []
todo = []
solo2 = []
for i in range(len(animales_frecuencias)):
    tormentas = False
    grillos = False
    zumbidos = False
    if animales_frecuencias[i][1][0] < Tormenta_eléctrica < animales_frecuencias[i][1][1]:
        tormenta.append(animales_frecuencias[i][0])
        tormentas = True
    if animales_frecuencias[i][1][0] < Grillos_en_la_noche < animales_frecuencias[i][1][1]:
        grillo.append(animales_frecuencias[i][0])
        grillos = True
    if animales_frecuencias[i][1][0] < Zumbido_en_colmena_de_abejas < animales_frecuencias[i][1][1]:
        zumbido.append(animales_frecuencias[i][0])
        zumbidos = True
    if tormentas is True and grillos is True and zumbidos is True:
        todo.append(animales_frecuencias[i][0])
    if tormentas is True and grillos is True:
        solo2.append(animales_frecuencias[i][0])
print(tormenta, "pueden escuchar las tormentas")
print(grillo, "pueden escuchar los grillos")
print(zumbido, "pueden escuchar los zumbidos")
print(todo, "pueden escuchar las 3 cosas")
print(solo2, "pueden escuchar las tormentas y los grillos")
