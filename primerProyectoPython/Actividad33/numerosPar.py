# ‐*‐ coding: utf‐8 ‐*‐

def calcularPares(_numeroUno, _numeroDos):
    for i in range (_numeroUno, _numeroDos+1):
        if (i%2 == 0):
            print i, "es par"
        else:
            print i, "no es par"

numeroUno = input("Introduce el primer número: ")

numeroDos = input("Introduce el segundo número: ")

calcularPares(numeroUno, numeroDos)
