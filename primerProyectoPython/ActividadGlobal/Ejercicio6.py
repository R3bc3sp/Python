# ‐*‐ coding: utf‐8 ‐*‐

archivo = open("numeros.txt", "r")
numeros = archivo.readline()
archivo.close()

numerosLista = map(int, numeros.split())  # Map convierte los strings a int
numerosSuma = sum(numerosLista)

archivo = open("numerosSuma.txt", "w")
archivo.write(str(numerosSuma))
archivo.close()