# ‐*‐ coding: utf‐8 ‐*‐

def getDivisores(n):
    divisores = []
    try:
        assert(n >= 25 and isinstance(n, int))
        for i in range(n):
            if (n % (i+1) == 0):
                divisores.append(i+1)
        return divisores
    except AssertionError:
        return "Ha ingresado un valor incorrecto. El valor debe ser un número entero mayor de 25"

try:
    numero = input("Introduce un número: ")
    print getDivisores(numero)
except NameError:
    print "El valor introducido ha de ser un dígito"
