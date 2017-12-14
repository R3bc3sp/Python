# ‐*‐ coding: utf‐8 ‐*‐

numeroUno = input("Introduce el primer número: ")
numeroDos = input("Introduce el segundo número: ")

total = 0
pares = 0
impares = 0
sumaPares = 0

for i in range(min(numeroUno, numeroDos), (max(numeroUno, numeroDos)+1)):
    print i
    total += 1
    if (i%2 == 0):
        pares += 1
        sumaPares += i
    else:
        impares += 1

print "Pares:", pares
print "Impares:", impares
print "Suma de los pares:", sumaPares
print "Números en total:", total