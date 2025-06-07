listaTareas = []
def agregarTarea(titulo, fecha):
    tarea = {"titulo": titulo, "fecha": fecha, "completada": False}
    listaTareas.append(tarea)
    print("Tarea agregada exitosamente")
def mostrarTareas():
    print("Tareas:")
    for i in range(0, len(listaTareas) + 1):
        tarea = listaTareas[i]
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i}. {tarea['titulo']} - {estado}")
def completarTarea(numero):
    listaTareas[numero]["completada"] = True
    print("Tarea marcada como completada")
def eliminarTarea(titulo):
    for tarea in listaTareas:
        if tarea["titulo"] == titulo:
            listaTareas.remove(tarea)
            print("Tarea eliminada")
        else:
            print("Tarea no encontrada")
def main():
    agregarTarea("Estudiar", "2025-06-01")
    agregarTarea("Sacar la basura", "2025-06-02")
    mostrarTareas()
    completarTarea(0)
    eliminarTarea("Dormir")
    mostrarTareas()
main()
