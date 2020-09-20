import unittest
from Punto import punto
from Triangulo import triangulo
from math import pi

class TestCirculo(unittest.TestCase):

    def test_calcularArea(self):
        t = triangulo(punto(0,1),punto(4,0),punto(4,2))
        area = t.calcularArea()
        self.assertEquals(area, 4)
        
if __name__ == "__main__":
    unittest.main()