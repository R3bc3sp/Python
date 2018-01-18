# ‐*‐ coding: utf‐8 ‐*‐

def calcularFibonacciSinExcepciones(n):
    if n >= 20 or n <= 0:
        print "Ha ingresado un valor incorrecto. El valor debe ser un número entero mayor que 0 y menor que 20"
        return
    
    salida=[]
    a,b = 0,1
    for x in range(n):
        salida.append(b)
        a, b = b, a+b
    
    return salida

def mainSinExcepciones():
    try:
        n = input("Ingrese n para calcular Fibonacci: ")
        print calcularFibonacciSinExcepciones(n)
    except NameError as e:
        print "Introduce un digito"

mainSinExcepciones()