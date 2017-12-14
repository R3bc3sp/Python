# ‐*‐ coding: utf‐8 ‐*‐

multiplos = 0
sumaMultiplos = 0

numero = input("Introduce un número: ")

for i in range(1, (numero+1)):
    if (i%2 == 0 and i%3 == 0):
        print i
        multiplos += 1
        sumaMultiplos += i

print "Multiplos de 2 y 3:", multiplos
print "Suma de los multiplos de 2 y 3:", sumaMultiplos