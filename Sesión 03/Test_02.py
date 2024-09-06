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
carro1.acelerar()
carro1.acelerar()
print("La velocidad actual del carro1 es: {}".format(carro1.velocidad))
carro1.frenar()
print("La velocidad despues de frenar del carro1 es: {}".format(carro1.velocidad))