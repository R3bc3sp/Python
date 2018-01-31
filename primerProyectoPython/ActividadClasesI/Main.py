# ‐*‐ coding: utf‐8 ‐*‐

from Alumno import Alumno
from Termo import Termo

alumno = Alumno("Ivan")
alumno.addDeporte("futbol")
alumno.addDeporte("basket")
alumno.addDeporte("golf")

print alumno

termo = Termo(1)
termo.beber()