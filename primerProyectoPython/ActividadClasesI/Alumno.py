# ‐*‐ coding: utf‐8 ‐*‐

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.deportes = []
    
    def addDeporte(self, deporte):
        self.deportes.append(deporte)
    
    def __str__(self):
        str1 = self.nombre + " practica " + ', '.join(self.deportes)
        return str1
