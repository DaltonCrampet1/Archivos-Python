#!/usr/bin/env python3
import json
import base64
import sys
import os
from PIL import Image
import io

# Paleta RGB fija
PALETA_RGB_VALIDOS = {
    (255, 0, 0): 2,       # Rojo
    (0, 0, 255): 4,       # Azul
    (255, 255, 0): 3,     # Amarillo
    (0, 255, 0): 1,       # Verde
    (255, 0, 255): 6,     # Lila
    (0, 255, 255): 5,     # Cian
    (255, 255, 255): 7,   # Blanco
    (0, 0, 0): 0          # Negro
}

def leer_coordenadas_txt(ruta_archivo):
    coordenadas = []
    max_x = 0
    max_y = 0

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()

        if '.db' in contenido:
            return leer_formato_db(contenido)

        lineas = contenido.strip().split('\n')

        for num_linea, linea in enumerate(lineas, 1):
            linea = linea.strip()
            if not linea or linea.startswith('#'):
                continue

            try:
                if ',' in linea:
                    partes = [p.strip() for p in linea.split(',')]
                else:
                    partes = linea.split()

                if len(partes) >= 5:
                    x = int(partes[0])
                    y = int(partes[1])
                    r, g, b = int(partes[2]), int(partes[3]), int(partes[4])
                    color = (r, g, b)

                    if color not in PALETA_RGB_VALIDOS:
                        print(f"Color no válido en línea {num_linea}: {color}")
                        continue

                    coordenadas.append((x, y, color))
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

            except ValueError as e:
                print(f"Error en línea {num_linea}: {linea} - {e}")
                continue

        ancho = max_x + 1 if coordenadas else 32
        alto = max_y + 1 if coordenadas else 32

        return coordenadas, ancho, alto

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None, 0, 0

def leer_formato_db(contenido):
    coordenadas = []
    lineas = contenido.strip().split('\n')

    color_map = {
        '0x0': (0, 0, 0, 255),           # Negro
        '0x1': (0, 255, 0, 255),         # Verde
        '0x2': (255, 0, 0, 255),         # Rojo
        '0x3': (255, 255, 0, 255),       # Amarillo
        '0x4': (0, 0, 255, 255),         # Azul
        '0x5': (0, 255, 255, 255),       # Cian
        '0x6': (255, 0, 255, 255),       # Lila
        '0x7': (255, 255, 255, 255),     # Blanco
    }

    y = 0
    max_x = 0

    for linea in lineas:
        if linea.startswith('.db'):
            valores = linea.replace('.db ', '').split(', ')
            for x, valor in enumerate(valores):
                color = color_map.get(valor.strip())
                if color is not None:
                    coordenadas.append((x, y, color))
                    max_x = max(max_x, x)
            y += 1

    ancho = max_x + 1 if coordenadas else 32
    alto = y if y > 0 else 32

    return coordenadas, ancho, alto

def convertir_color(color):
    if isinstance(color, (tuple, list)):
        if len(color) == 3:
            rgba = tuple(color) + (255,)
        elif len(color) == 4:
            rgba = tuple(color)
        else:
            return (0, 0, 0, 255)

        if rgba[:3] in PALETA_RGB_VALIDOS:
            return rgba
    return (0, 0, 0, 255)

def coordenadas_a_piskel_txt(coordenadas_colores, ancho=32, alto=32, nombre="Sprite"):
    imagen = Image.new('RGBA', (ancho, alto), (0, 0, 0, 0))
    pixels = imagen.load()

    for coord in coordenadas_colores:
        if len(coord) >= 3:
            x, y, color = coord
            if 0 <= x < ancho and 0 <= y < alto:
                rgba_color = convertir_color(color)
                pixels[x, y] = rgba_color

    buffer = io.BytesIO()
    imagen.save(buffer, format='PNG')
    png_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    base64_png = f"data:image/png;base64,{png_data}"

    piskel_data = {
        "modelVersion": 2,
        "piskel": {
            "name": nombre,
            "description": "",
            "fps": 0,
            "height": alto,
            "width": ancho,
            "layers": [
                f'{{"name":"Layer 1 (imported)","opacity":1,"frameCount":1,"chunks":[{{"layout":[[0]],"base64PNG":"{base64_png}"}}]}}'
            ],
            "hiddenFrames": [""]
        }
    }

    return json.dumps(piskel_data, separators=(',', ':'))

def main():
    if len(sys.argv) != 3:
        print("Uso: python convertidor_piskel.py <archivo_entrada.txt> <archivo_salida.piskel>")
        return

    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    # Forzar extensión .piskel
    if not archivo_salida.endswith('.piskel'):
        archivo_salida = os.path.splitext(archivo_salida)[0] + '.piskel'

    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
        return

    print(f"Leyendo archivo: {archivo_entrada}")
    coordenadas, _, _ = leer_coordenadas_txt(archivo_entrada)

    if not coordenadas:
        print("No se encontraron coordenadas válidas en el archivo.")
        return

    # Compactar al origen
    min_x = min(x for x, _, _ in coordenadas)
    min_y = min(y for _, y, _ in coordenadas)
    coordenadas = [(x - min_x, y - min_y, color) for x, y, color in coordenadas]

    ancho, alto = 32, 32

    print("Generando archivo Piskel...")
    nombre_sprite = os.path.splitext(os.path.basename(archivo_entrada))[0]
    piskel_json = coordenadas_a_piskel_txt(coordenadas, ancho, alto, nombre_sprite)

    try:
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            f.write(piskel_json)
        print(f"✅ Archivo guardado como: {archivo_salida}")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

if __name__ == "__main__":
    main()

# Convierte 0x0 a piskel
# python convertidor_piskel.py entrada.txt sprite

