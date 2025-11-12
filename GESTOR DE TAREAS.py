import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo hay tareas pendientes.")
    else:
        print("\n📋 Lista de tareas:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Escribe el nombre de la tarea: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Tarea agregada exitosamente.")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nNúmero de tarea a marcar como completada: ")) - 1
        tasks[num]["done"] = True
        save_tasks(tasks)
        print("Tarea marcada como completada.")
    except (ValueError, IndexError):
        print("Número inválido.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("\nNúmero de tarea a eliminar: ")) - 1
        deleted = tasks.pop(num)
        save_tasks(tasks)
        print(f"Tarea '{deleted['title']}' eliminada.")
    except (ValueError, IndexError):
        print("Número inválido.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== GESTOR DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        option = input("Selecciona una opción: ")
        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            add_task(tasks)
        elif option == "3":
            complete_task(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
