# ‐*‐ coding: utf‐8 ‐*‐

pares = 0
impares = 0

for i in range(1, 101):
    print i
    if (i%2 == 0):
        pares += 1
    else:
        impares += 1

print "Pares", pares
print "Impares", impares