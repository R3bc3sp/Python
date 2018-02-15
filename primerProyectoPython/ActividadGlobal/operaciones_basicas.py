# ‐*‐ coding: utf‐8 ‐*‐

def sumar(s1, s2):
    return s1+s2

def restar(r1, r2):
    return r1-r2

def multiplicar(m1, m2):
    return m1*m2

def dividir(d1, d2):
    try:
        return d1/d2
    except ZeroDivisionError:
        return "El divisor no puede ser cero"