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
