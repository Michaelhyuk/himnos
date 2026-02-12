import os
import re

# Corre esto en tu carpeta de himnos para que Android los acepte
for archivo in os.listdir('.'):
    if archivo.endswith(".mp3"):
        # Lo vuelve minúsculas y cambia espacios por guiones bajos
        nuevo = archivo.lower().replace(" ", "_")
        nuevo = re.sub(r'[^a-z0-9_.]', '', nuevo)
        # Android no deja que empiecen con número: le ponemos una 'h'
        if nuevo[0].isdigit(): nuevo = "h" + nuevo
        os.rename(archivo, nuevo)
print("✅ ¡Archivos listos para Android!")