# ‐*‐ coding: utf‐8 ‐*‐

vocales = ["a", "e", "i", "o", "u"]

texto = raw_input("Introduce texto: ")

for i in range(len(texto)):
    if (texto[i] in vocales):
        print texto[i], "es vocal"
    else:
        print texto[i], "es consonante"