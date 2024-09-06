"""
Programación orientada a objetos
"""
from operator import truediv

from sqlalchemy import false


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

"""Aplicando herencia"""
"""Creamos una clase hija"""

class CarroVolador(Carro):
    ruedas = 6
    def __init__(self, color, aceleracion, estadovolando = False):
        super().__init__(color, aceleracion)
        #self.estadovolando = estadovolando
        #self.aceleracion = aceleracion

    def vuela(self):
        self.estadovolando = True


    def aterriza(self):
        self.estadovolando = False

carro1 = Carro("Rojo", 45)
#carro1.color = "Rojo"
#carro1.aceleracion = 45

carroVol = CarroVolador("Blanco",55)
carroVol.vuela()
print("El estado actual del carro volador es: {}".format(carroVol.estadovolando))
carroVol.aterriza()
print("El estado actual del carro volador es: {}".format(carroVol.estadovolando))