#error 1
numero = 7/0
#error 2
lista = [4, 7, 30, 23, 5]

lista[10]
#error 3
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 

paises["alemania"]
#error 4
resultado = "2" + 10

class Errores():
    def __init__(self,error1,error2,error3,error4):
        self.error1 = error1
        self.error2 = error2
        self.error3 = error3
        self.error4 = error4
    def errores(self,error1,error2,error3,error4):
        try:
            error1
        except ZeroDivisionError:
            print("No podemos dividir 7 entre 0")
        try:
            error2
        except IndexError:
            print("El índice que piden no está en lista")
        try:
            error3
        except KeyError:
            print("El país no está en el diccionario")
        try:
            error4
        except TypeError:
            print("No puedes sumar nada que sea tipo str")
