from Tarea import Tareas

listarTareas = [Tareas("Tarea 1"), Tareas("Tarea 2"), Tareas("Tarea 3")]
Tareas.listar(listarTareas)
listarTareas[0].completar()
Tareas.listar(listarTareas)
print("ola mundo")