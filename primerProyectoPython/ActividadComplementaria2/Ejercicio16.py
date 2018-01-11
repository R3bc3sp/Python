# ‐*‐ coding: utf‐8 ‐*‐

lista1 = ["se", "mamut"]
lista2 = ["as", "de", "mi"]

def algoEnComun(lista1, lista2):
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if (lista1[i] == lista2[j]):
                print "True"
                return
    print "False"

algoEnComun(lista1, lista2)