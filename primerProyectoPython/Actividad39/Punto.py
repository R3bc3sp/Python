# ‐*‐ coding: utf‐8 ‐*‐
import math

class Punto(object):
    # Representación de las coordenadas cartesianas
    def __init__(self, x=0, y=0):
        # Constructor de Punto, x e y deben ser numéricos
        if (self.es_numero(x) and self.es_numero(y)):
            self.x = x
            self.y = y
        else:
            raise TypeError("Debes introducir dos digitos")
    
    def es_numero(self, num):
        if (isinstance(num, (int, float, long))):
            return True
        else:
            return False
    
    def restar(self, punto):
        puntoRes = Punto(self.x - punto.x, self.y - punto.y)
        return puntoRes
    
    def norma_vector(self):
        vector = math.sqrt(self.x**2 + self.y**2)
        return vector
    
    def distancia_punto(self, punto):
        distancia = math.sqrt((punto.x - self.x)**2 + (punto.y - self.y)**2)
        return distancia
    
    def mostrar_coordenadas(self):
        print "(", self.x, ",", self.y, ")"

punto = Punto(1, 1)

punto.mostrar_coordenadas()