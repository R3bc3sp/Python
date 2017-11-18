# ‐*‐ coding: utf‐8 ‐*‐

import math

def calcularFactorial(_veces):
    for i in range(_veces):
        numero = input("Introduce numero para calcular su factorial: ")
        print "El factorial de", numero, "es", math.factorial(numero)

veces = input("Introduce cantidad de valores a ingresar: ")

calcularFactorial(veces)