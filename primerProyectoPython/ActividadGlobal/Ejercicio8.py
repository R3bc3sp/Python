# ‐*‐ coding: utf‐8 ‐*‐

def getElemento(l, i):
    try:
        return l[i]
    except IndexError:
        return None

lista = []
elementos = input("Introduce número de elementos: ")

for i in range(elementos):
    lista.append(raw_input("Elemento "+str(i)+": "))

indice = input("Introduce el índice: ")

print getElemento(lista, indice)