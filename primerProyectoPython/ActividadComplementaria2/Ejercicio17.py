# ‐*‐ coding: utf‐8 ‐*‐

numeros = [3, 1, 7, 5, 20, 14]

def max_in_list(lista):
    mayor = 0
    for i in range(len(lista)):
        if (lista[i] > mayor):
            mayor = lista[i]
    print mayor

max_in_list(numeros)