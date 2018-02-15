# ‐*‐ coding: utf‐8 ‐*‐

import operaciones_basicas as ob
from operaciones_basicas import sumar, restar, multiplicar, dividir

try:
    n1 = input("Introduce número 1: ")
    n2 = input("introduce número 2: ")
    
    # Parte A del ejercicio 10
    print
    print "Operandos =", n1, "&", n2
    print "Sumar =", ob.sumar(n1, n2)
    print "Restar =", ob.restar(n1, n2)
    print "Multiplicar =", ob.multiplicar(n1, n2)
    print "Dividir =", ob.dividir(n1, n2)
    
    # Parte B del ejericio 10
    print
    print "Operandos =", n1, "&", n2
    print "Sumar =", sumar(n1, n2)
    print "Restar =", restar(n1, n2)
    print "Multiplicar =", multiplicar(n1, n2)
    print "Dividir =", dividir(n1, n2)
except NameError:
    print "Debes introducir un digito"


