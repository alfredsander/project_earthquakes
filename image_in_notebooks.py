# Este script permite imprimir imagenes a partir de URLs en jupyter notebooks.
# La biblioteca PIL funciono de tres intentos.
import requests
from IPython.display import display
from PIL import Image
from io import BytesIO
import re

# URL de la imagen que deseas abrir
url = "https://i.scdn.co/image/ab67616d0000b2730656d5ce813ca3cc4b677e05"

# Descarga los datos de la imagen desde la URL
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    # Abre la imagen utilizando PIL y la muestra en el cuaderno
    img = Image.open(BytesIO(response.content))
    display(img)
else:
    print("No se pudo obtener la imagen desde la URL.")
