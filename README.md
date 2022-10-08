<h1 align="center">	Evaluacion Tema 2</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/carmenm02/EvaluacionTema2.git)

```
## Ejercicio1 :

class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)
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
```
```
## Ejercicio2:

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
```
```
## Ejercicio3:

class Producto:
    def __init__(self,codigo,nombre,precio,tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    def __str__(self):
        return" El código {} de nombre {} tiene un precio igual a {} y es de tipo {}".format(self.codigo,self.nombre,self.precio,self.tipo)
    def imprimir(self,producto1):
        if producto1 == Producto(1,"Iphone",599.9,"smarthphone"):
            print(producto1)
        else:
            print(producto2)
    
producto1 = Producto(1,"Iphone",599.9,"smarthphone")

producto2 = Producto(2,"Ipad",699,"tablet")
```
```
## Ejercicio4:

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
```
```
## Ejercicio5:

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
```
