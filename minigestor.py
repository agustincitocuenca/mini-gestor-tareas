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
        
# Agrega una nueva tarea pendiente
def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ").strip()
    if descripcion:
        tareas.append({'descripcion': descripcion, 'completada': False})
        print("✅ Tarea agregada.")
    else:
        print("❌ La descripción no puede estar vacía.")

# Lista todas las tareas con su estado
def listar_tareas(tareas):
    if not tareas:
        print("📭 No hay tareas registradas.")
        return
    print("\n📋 Lista de tareas:")
    for i, tarea in enumerate(tareas):
        estado = "✔ Completada" if tarea['completada'] else "⏳ Pendiente"
        print(f"{i + 1}. {tarea['descripcion']} [{estado}]")
        