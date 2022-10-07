class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
alumno1 = Alumno("fran",5)
alumno1.__init__("fran",5)
alumno1.imprimir()
