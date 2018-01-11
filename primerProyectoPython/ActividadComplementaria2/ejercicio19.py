# ‐*‐ coding: utf‐8 ‐*‐

palabras = ["palabra", "tierra", "esdrujula", "sol", "yate"]

def filtrar_palabras(lista, letras):
    palabras_new = []
    for i in range(len(lista)):
        if (len(lista[i]) > letras):
            palabras_new.append(lista[i])
    print palabras_new

filtrar_palabras(palabras, 4)