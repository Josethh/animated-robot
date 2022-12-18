# 1. Crea una clase Produtc con los siguientes atributos:
#     - Code 
#     - Name 
#     - Price
# Creale su constructor, getter, setter y una funcion llamada calcular_total,
# donde le pasaremos unas unidades y nos debe calcular el precio final.

class Product:
    
    def __init__(self, code, name, price):
        self.__code   = code 
        self.__name   = name 
        self.__price  = price 

    @property 
    def code(self):
        return self.__code

    @code.setter 
    def code(self, value):
        self.__code = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value 

    @property
    def price(self):
        return self.__price

    @price.setter 
    def price(self, value):
        self.__price = value 

    def calculate_total(self, units):
        return self.price * units

    def __str__(self):
        return 'Codigo: ' + str(self.__code) + ', Nombre: ' + str(self.__name) + ', Precio: ' + str(self.__price)


p1 = Product(1, 'Producto1', 6)
p2 = Product(2, 'Producto2', 12)
p3 = Product(3, 'Producto3', 54)

p1.name = 'Gafas'
p2.name = 'Libro'
p3.name = 'Carta'

print(p1.name)
print(p2.name)
print(p3.name)

print(p1)
print(p2)
print(p3)

print(p1.calculate_total(5))
print(p2.calculate_total(5))
print(p3.calculate_total(5))