# ‐*‐ coding: utf‐8 ‐*‐

elementos1 = input("Introduce numero de elementos para la lista 1: ")
elementos2 = input("Introduce numero de elementos para la lista 2: ")

lista1 = []
lista2 = []

print "Lista 1"
for i in range(elementos1):
    lista1.append(raw_input("Elemento "+str(i)+": "))

print "Lista 2"
for i in range(elementos2):
    lista2.append(raw_input("Elemento "+str(i)+": "))

listaComun = []
for i in lista1:
    if (i in lista2):
        listaComun.append(i)

print listaComun