from math import pi
from Punto import punto
class rectangulo():
    def __init__(self, p1,p2,p3,p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
    
    def hallarArea(self):
        d1 = self.p1.hallarDistancia(self.p2)
        d2 = self.p2.hallarDistancia(self.p3)
        d3 = self.p3.hallarDistancia(self.p4)
        d4 = self.p4.hallarDistancia(self.p1)

        if(d1==d2 and d3==d4):
            area= d1*d3
        if(d1==d3 and d2==d4):
            area= d1*d2
        if(d1==d4 and d2==d3):
            area= d1*d2
        return area
    def hallarPerimetro(self):
        d1 = self.p1.hallarDistancia(self.p2)
        d2 = self.p2.hallarDistancia(self.p3)
        d3 = self.p3.hallarDistancia(self.p4)
        d4 = self.p4.hallarDistancia(self.p1)
        periemtro= d1+d2+d3+d4
        return periemtro