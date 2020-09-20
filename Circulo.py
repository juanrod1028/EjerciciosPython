from math import pi
from Punto import punto
class circulo():
    def __init__(self, radio, centro):
        self.radio= radio
        self.centro= centro
    
    def hallarArea(self):
        area = pi*(self.radio**2)
        return area

    def hallarPerimetro(self):
        perimetro = pi*2*self.radio
        return perimetro

    def determinarPuntoDentro(self, p):
        distancia = self.centro.hallarDistancia(p)
        if (distancia < self.radio):
            return True
        else:
            return False