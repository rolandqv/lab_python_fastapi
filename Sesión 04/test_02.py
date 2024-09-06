"""Decoradores en Python"""
"""Creación interna de la función decoradora"""

def funcionA(funcionB):
    def funcionC(*args):
        print("1. Antes de ejecutar la función a decorar")
        resultado = funcionB(*args)
        print("2. Esto sucede luego de ejecutar la función a decorar")
        return resultado
    return funcionC


@funcionA
def suma(a, b):
    print(a + b)

suma(30,100)