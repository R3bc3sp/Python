# ‐*‐ coding: utf‐8 ‐*‐

class Videoclub(object):
    def __init__(self, lista=[], titulo="", precio="", isAlquilado=False):
        self.titulo = titulo
        self.precio = precio
        self.isAlquilado = isAlquilado
        self.lista = lista
    
    def alquiler(self):
        if (self.isAlquilado == False):
            self.isAlquilado = True
            return 1
        else:
            return 0
    
    def devolucion(self):
        if (self.isAlquilado == True):
            self.isAlquilado = False
            return 1
        else:
            return 0
    
    def mostrarDatos(self):
        print "------------------------------------------------------------------------"
        for x in self.lista:
            if (isinstance(x, Pelicula)):
                print "Pelicula =>", x
            elif (isinstance(x, Videojuego)):
                print "Videojuego =>", x
        print "------------------------------------------------------------------------"

class Videojuego(Videoclub):
    def __init__(self, titulo, precio, isAlquilado, codPegi, plataforma):
        Videoclub.__init__(self, None,  titulo, precio, isAlquilado)
        self.codPegi = codPegi
        self.plataforma = plataforma
    
    def __str__(self):
        return "Titulo: '%s' - Precio: %s - Alquilado: %s - PEGI: %s - Plataforma: %s" % (self.titulo, self.precio, str(self.isAlquilado), str(self.codPegi), self.plataforma)

class Pelicula(Videoclub):
    def __init__(self, titulo, precio, isAlquilado, genero, year, director):
        Videoclub.__init__(self, None, titulo, precio, isAlquilado)
        self.genero = genero
        self.year = year
        self.director = director
    
    def __str__(self):
        return "Titulo: '%s' - Precio: %s - Alquilado: %s - Genero: %s - Año: %s - Director: %s" % (self.titulo, self.precio, str(self.isAlquilado), self.genero, str(self.year), self.director)