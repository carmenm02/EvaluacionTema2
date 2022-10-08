class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):

        return "color {}, {} ruedas".format( self.color, self.ruedas )

coche = ("rojo",4)
bicicleta = ("negra",2)
lista = [coche.__dict__,bicicleta.__dict__]