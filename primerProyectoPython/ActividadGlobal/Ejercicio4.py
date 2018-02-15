# ‐*‐ coding: utf‐8 ‐*‐

archivo = open("archivo.txt", "r")
archivo_texto = archivo.readline()
archivo.close()

print len(archivo_texto)