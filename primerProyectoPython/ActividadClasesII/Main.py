# ‐*‐ coding: utf‐8 ‐*‐

from Clases import Videoclub, Pelicula, Videojuego

p1 = Pelicula("El Señor de los Anillos: El Retorno del Rey", "4€", True, "Aventuras", 2003, "Peter Jackson")
p2 = Pelicula("Titanic", "3€", False, "Drama", 1997, "James Cameron")
p3 = Pelicula("Skyfall", "3€", False, "Accion", 2012, "Sam Mendes")
vj1 = Videojuego("Call Of Duty: Black Ops III", "5€", True, 18, "PS4")
vj2 = Videojuego("Super Mario Bros", "4€", False, 3, "3DS")
vj3 = Videojuego("Just Dance 2016", "4€", True, 3, "WII")

lista = []
lista.append(p1)
lista.append(p2)
lista.append(p3)
lista.append(vj1)
lista.append(vj2)
lista.append(vj3)

vc = Videoclub(lista)

vc.mostrarDatos()

# Peliculas
if p1.alquiler(): print "Se ha alquilado correctamente"
else: print "No se ha podido alquilar"

if p2.alquiler(): print "Se ha alquilado correctamente"
else: print "No se ha podido alquilar"

if p3.devolucion(): print "Se ha devuelto correctamente"
else: print "No se ha podido devolver"

# Videojuegos
if vj1.devolucion(): print "Se ha devuelto correctamente"
else: print "No se ha podido devolver"

if vj2.alquiler(): print "Se ha alquilado correctamente"
else: print "No se ha podido alquilar"

if vj3.devolucion(): print "Se ha devuelto correctamente"
else: print "No se ha podido devolver"

vc.mostrarDatos()