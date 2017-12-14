# ‐*‐ coding: utf‐8 ‐*‐

valorA = input("Introduce valor A: ")
valorB = input("Introduce valor B: ")

if (valorA>=valorB):
    suma = 0
    for i in range(10, 51):
        suma += i
    
    print suma

elif (valorA/valorB <= 30):
    print (valorA**2+valorB**2)