# ‐*‐ coding: utf‐8 ‐*‐

def calcularFibonacciConExcepciones(n):
    try:
        assert not(n <= 0 or n >= 20)
        salida=[]
        a,b = 0,1
        for x in range(n):
            salida.append(b)
            a, b = b, a+b
    except AssertionError:
        print "Ha ingresado un valor incorrecto. El valor debe ser un número entero mayor que 0 y menor que 20"

    return salida

def mainConExcepciones():
    try:
        n = input("Ingrese n para calcular Fibonacci: ")
        print calcularFibonacciConExcepciones(n)
    except NameError:
        print "Introduce un digito"

mainConExcepciones()