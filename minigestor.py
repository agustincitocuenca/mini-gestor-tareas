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

# Marca una tarea como completada
def completar_tarea(tareas):
    listar_tareas(tareas)
    if not tareas:
        return
    try:
        num = int(input("Ingrese el número de la tarea a completar: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]['completada'] = True
            print("✅ Tarea marcada como completada.")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

# Elimina una tarea
def eliminar_tarea(tareas):
    listar_tareas(tareas)
    if not tareas:
        return
    try:
        num = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            eliminada = tareas.pop(num - 1)
            print(f"🗑 Tarea eliminada: {eliminada['descripcion']}")
        else:
            print("❌ Número inválido.")
    except ValueError:
        print("❌ Entrada inválida.")

# Menú principal con decoración
def menu():
    tareas = cargar_tareas()
    while True:
        print(f"\n{AZUL}=== 📝 Mini Gestor de Tareas ==={RESET}")
        print("1️⃣  Agregar tarea")
        print("2️⃣  Listar tareas")
        print("3️⃣  Completar tarea")
        print("4️⃣  Eliminar tarea")
        print("5️⃣  Salir")

        opcion = input(f"{AMARILLO}Seleccione una opción: {RESET}")

        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            listar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            guardar_tareas(tareas)
            print(f"{VERDE}👋 ¡Hasta luego! Tus tareas se han guardado.{RESET}")
            break
        else:
            print(f"{ROJO}❌ Opción inválida. Intente nuevamente.{RESET}")

if __name__ == "__main__":
    menu()
