# ‐*‐ coding: utf‐8 ‐*‐

# Hay que usar raw_input cuando se quieren obtener strings
nombre = raw_input("¿Cómo te llamas?: ")
print "Bienvenido", nombre.capitalize()

years = input("¿Cuántos años tienes?: ")
print "Tienes", years ,"años"

print "Tu nombre tiene", len(nombre) ,"caracteres"