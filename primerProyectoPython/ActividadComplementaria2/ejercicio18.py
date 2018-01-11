# ‐*‐ coding: utf‐8 ‐*‐

palabras = ["palabra", "tierra", "esdrujula", "sol", "yate"]

def mas_larga(lista):
    palabra = ""
    letras = 0
    for i in range(len(lista)):
        if (len(lista[i]) > letras):
            letras = len(lista[i])
            palabra = lista[i]
    print palabra

mas_larga(palabras)