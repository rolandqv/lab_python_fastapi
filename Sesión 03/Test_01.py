"""
Programación orientada a objetos
"""
class Carro:
    """Atributos"""
    ruedas = 4
    """Constructor: valores que van ha tener por defecto mi clase que se le instanciará a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0
    """Métodos son las funciones de la clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

"""Instanciamos nuestra clase"""
carro1 = Carro("Negro",50)
print(carro1.color)
print(carro1.aceleracion)
print(carro1.ruedas)

carro2 = Carro("Rojo",70)
print(carro2.color)
print(carro2.aceleracion)
print(carro2.ruedas)

carro2.marchas = 2000
print("El número de marchas de mi carro 2 es : {}".format(carro2.marchas))



#"""Otra forma"""
#carro2 = Carro()
#carro2.color = "AZUL"
#carro2.aceleracion = "100"
#print(carro2.color)
#print(carro2.aceleracion)
