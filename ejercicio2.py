class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
    def __str__(self):
        return "{} ha sacado un {}".format(self.nombre,self.nota)
    def calificación(self):
        if self.nota >= 5:
            print("Aprobado")
        else:
            print("Suspenso")
alumno = Alumno("fran",5)
alumno.__init__("fran",5)
alumno.imprimir()
alumno.calificación()

alumna = Alumno("carmen",7)
alumna.__init__("carmen",7)
alumna.imprimir()
alumna.calificación()