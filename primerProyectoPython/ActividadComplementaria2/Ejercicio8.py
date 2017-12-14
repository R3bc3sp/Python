# ‐*‐ coding: utf‐8 ‐*‐

suma = 0

for i in range(100, 0, -1):
    suma += i
    if (i%2 != 0):
        print i

print "Suma:", suma