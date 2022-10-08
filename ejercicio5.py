class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )

class Coche(Vehiculo):

     def __init__(self, color, ruedas, velocidad, cilindrada):

        Vehiculo.__init__(self, color, ruedas)

        self.velocidad = velocidad

        self.cilindrada = cilindrada

def __str__(self):
    return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


class Bicicleta():

    def __init__(self,color,ruedas,tipo):

        Vehiculo.__init__(self, color, ruedas)

        self.tipo = tipo
    
def __str__(self):
    return Vehiculo.__str__(self) + ", {}".format(self.tipo)
    
def catalogar(self,lista):
    for vehiculo in lista:
        print(type(vehiculo).__name__,vehiculo.__dict__)



c = Coche("azul", 4, 150, 1200)
b = Bicicleta("negra",2,"bicicleta de montaña")
lista = [b,c]
print(lista)