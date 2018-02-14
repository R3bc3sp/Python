# ‐*‐ coding: utf‐8 ‐*‐

texto = raw_input("Introduce texto: ")

lista = texto.split()

for i in range(len(lista)):
    print i, lista[i],
    if (len(lista[i]) <= 5):
        print "=> corta"
    else:
        print "=> larga"