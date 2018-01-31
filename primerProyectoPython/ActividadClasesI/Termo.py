# ‐*‐ coding: utf‐8 ‐*‐

class Termo:
    def __init__(self, cantidadCafe):
        if (isinstance(cantidadCafe, (int, float, long))):
            if (cantidadCafe >= 0 and cantidadCafe <= 10):
                self.cantidadCafe = cantidadCafe
                self.isFull = False
            else:
                raise TypeError("El dígito debe estar comprendido entre 0 y 10 (inclusives)")
        else:
            raise TypeError("Debes introducir un dígito")
    
    def rellenar(self):
        if (self.cantidadCafe < 10):
            self.cantidadCafe += 1
        else:
            raise TypeError("¡Cuidado!¡Se desbordará!")
    
    def beber(self):
        if (self.cantidadCafe > 0):
            self.cantidadCafe -= 1
        else:
            raise TypeError("¡El termo está vacío!")

