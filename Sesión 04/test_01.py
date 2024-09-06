"""Decoradores en Python"""
"""Creación interna de la función decoradora"""

def funcionA(funcionB):
    def funcionC():
        print("1. Antes de ejecutar la función a decorar")
        funcionB()
        print("2. Esto sucede luego de ejecutar la función a decorar")
    return funcionC()

@funcionA
def saludo():
    print("Hola Python")

#saludo()

