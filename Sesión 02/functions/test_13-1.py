"""
Programación funcional en Python

Ejercicio en clase
"""

"""
Requisitos:
- Solicitar al usuario 4 números por consola
- Crear una función que devuelva cuál es el mayor número de los 4 ingresado por el usuario
- Finalmente elevar al cubo este resultado
"""
num1 = input("Digitar numero1: ")
num2 = input("Digitar numero2: ")
num3 = input("Digitar numero3: ")
num4 = input("Digitar numero4: ")

def mayor_numero(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)

mayor = float(mayor_numero(num1, num2, num3, num4))

print("El mayor numero es: {}".format(mayor))
print("El cubo del mayor numero es: {}".format(mayor*mayor*mayor))





