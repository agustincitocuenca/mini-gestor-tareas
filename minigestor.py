import json
import os

ARCHIVO = 'tareas.json'

# Carga las tareas desde el archivo si existe, o devuelve una lista vacía
def cargar_tareas():
    if os.path.exists(ARCHIVO):
        try:
            with open(ARCHIVO, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

# Guarda las tareas en el archivo
def guardar_tareas(tareas):
    with open(ARCHIVO, 'w') as f:
        json.dump(tareas, f, indent=4)