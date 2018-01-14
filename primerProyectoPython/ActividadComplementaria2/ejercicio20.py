# ‐*‐ coding: utf‐8 ‐*‐

year = input("Introduce el año: ")

persona1 = [raw_input("Introduce el nombre: "), input("Introduce el año de nacimiento: ")]
persona2 = [raw_input("Introduce el nombre: "), input("Introduce el año de nacimiento: ")]
persona3 = [raw_input("Introduce el nombre: "), input("Introduce el año de nacimiento: ")]

edad = year - persona1[1]
print persona1[0], "cumplira", edad, "años"

edad = year - persona2[1]
print persona2[0], "cumplira", edad, "años"

edad = year - persona3[1]
print persona3[0], "cumplira", edad, "años"