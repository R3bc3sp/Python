# ‐*‐ coding: utf‐8 ‐*‐

valorA = input("Introduce valor A: ")
valorB = input("Introduce valor B: ")
valorC = input("Introduce valor C: ")

if (valorA/valorB > 30):
    print ((valorA/valorC*valorB)**3)

elif (valorA/valorB <= 30):
    suma = 0
    for i in range(2, 31, 2):
        suma = i**2
    
    print suma