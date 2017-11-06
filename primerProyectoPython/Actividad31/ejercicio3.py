# ‐*‐ coding: utf‐8 ‐*‐

cantidad = 0
iteraciones = 0

# Bucle for con 2 parámetros
for i in range(1, 501):
    if i % 7 == 0:
        print "Multiplo de 7: " + str(i)
        cantidad += 1
    iteraciones += 1

print "Se han encontrado " + str(cantidad) + " múltiplos de 7 en " + str(iteraciones) + " iteraciones"

cantidad = 0
iteraciones = 0

# Bucle for con 3 parámetros
for i in range(0, 501, 7):
    if i != 0:
        if i % 7 == 0:
            print "Multiplo de 7: " + str(i)
            cantidad += 1
    iteraciones += 1

print "Se han encontrado " + str(cantidad) + " múltiplos de 7 en " + str(iteraciones) + " iteraciones"