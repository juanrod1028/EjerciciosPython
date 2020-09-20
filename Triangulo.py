from Punto import punto
import math


class triangulo:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def calcularArea(self):
        a = self.p1.hallarDistancia(self.p2)
        b = self.p2.hallarDistancia(self.p3)
        c = self.p1.hallarDistancia(self.p3)

        if(a==b and a==c):#Equilatero
            area= ((3**(1/2))/4)*(a**2)
        if(a==c and a!=b):#Isocele
            area= (b*((a**2)-((b**2))/4)**(1/2))/2
        if(a==b and a!=c):#Isocele
            area= (c*((a**2)-((c**2))/4)**(1/2))/2
        if(b==c and b!=a):#Isocele
            area= (a*((b**2)-((a**2))/4)**(1/2))/2
        if(a!=b and a!=c):#equilatero
            semiPerimetro=(a+b+c)/2
            area= (semiPerimetro*(semiPerimetro-a)*(semiPerimetro-b)*(semiPerimetro-c))**(1/2)
            
        return area
    
