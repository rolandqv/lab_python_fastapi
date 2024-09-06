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
def comparar_mayor():
    n_mayor = 0
    k = 1
    c = int(input("Escriba la cantidad de numeros que desea comparar: "))
    while k<=c:
        n = float(input("Digitar numero: "))
        if n>n_mayor:
            n_mayor = n
        else:
            n_mayor = n_mayor
        k = k+1
    print("El mayor numero es: {}".format(n_mayor))
    print("El cubo del mayor numero es: {}".format(n_mayor*n_mayor*n_mayor))
    return
comparar_mayor()



