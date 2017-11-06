# ‐*‐ coding: utf‐8 ‐*‐


bicicleta = 5785.0
descuento = 38.0

resultado = bicicleta - (bicicleta * (descuento / 100))

print "El precio de la bicicleta con descuento es: " + str(resultado)
'''
while True:
    entrada = raw_input("> ")
    if entrada == "adios":
        break
    else:
        print entrada
'''       
'''
mi_lista = ['Juan', 'Antonio', 'Pedro', 'Luis']
for nombre in mi_lista:
    print nombre
for i in "AMIGO":
    print i
    print "¡AMIGO!"
for i in range(1, 10):
    print i*5

for i in range(2, 10, 2):
    print i
for i in range(2, 10, 3):
    print i
for i in range(10, 5, -1):
    print i
for i in range(3, -1, -1):
    print i
'''