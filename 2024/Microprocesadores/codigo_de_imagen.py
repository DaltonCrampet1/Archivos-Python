from PIL import Image
import numpy as np
import os

# Definir los colores básicos y sus valores
color_map = {
    (255, 0, 0): 2,      # Rojo
    (0, 0, 255): 4,      # Azul
    (255, 255, 0): 3,    # Amarillo
    (0, 255, 0): 1,      # Verde
    (255, 0, 255): 6,    # Lila
    (0, 255, 255): 5,    # Cian
    (255, 255, 255): 7,  # Blanco
    (0, 0, 0): 0         # Apagado
}

# Función para encontrar el color más cercano
def closest_color(rgb):
    r, g, b = rgb
    min_distance = float('inf')
    closest = None
    for color in color_map.keys():
        distance = np.sqrt((color[0] - r)**2 + (color[1] - g)**2 + (color[2] - b)**2)
        if distance < min_distance:
            min_distance = distance
            closest = color
    return closest

# Función para redimensionar la imagen y aproximar los colores
def process_image(image_path, output_text_path):
    if not os.path.exists(image_path):
        print(f"Error: El archivo {image_path} no existe.")
        return
    
    image = Image.open(image_path)
    image = image.resize((32, 32))  # Redimensionar la imagen a 32x32
    image = image.convert("RGB")  # Asegurarse de que la imagen esté en modo RGB
    
    pixel_values = []
    for y in range(32):
        row = []
        for x in range(32):
            rgb = image.getpixel((x, y))
            closest = closest_color(rgb)
            row.append(color_map[closest])
        pixel_values.append(row)
    
    # Guardar los valores en un archivo de texto
    with open(output_text_path, 'w') as f:
        for row in pixel_values:
            f.write('.db 0x')
            f.write(', 0x'.join(map(str, row)) + '\n')
            

# Ejemplo de uso
# dir
# cd nombre
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Uso: python codigo_de_imagen.py <ruta_de_imagen> <ruta_salida_txt>")
    else:
        process_image(sys.argv[1], sys.argv[2])

# Convierte imagen(32x32 recomendado) a 0x0
# python codigo_de_imagen.py entrada.png/jpg salida
