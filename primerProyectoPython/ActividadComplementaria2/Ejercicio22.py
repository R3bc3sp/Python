# ‐*‐ coding: utf‐8 ‐*‐

nombres = ["ivan", "christian", "maria", "rocio", "carlos", "andrea", "angel"]

letra = raw_input("Elige una letra: ")

for i in range(len(nombres)):
    if (nombres[i].startswith(letra)):
        print nombres[i]