class Tareas:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.completado = False
    
    def __str__(self):
        return f"Tarea: {self.nombre}, Completado: {self.completado}"   
    
    def listar(lista):
        for tarea in lista:
            print(tarea)
    
    def completar(self):
        self.completado = True
    