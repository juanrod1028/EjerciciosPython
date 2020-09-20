import unittest
from Punto import punto
from Rectangulo import rectangulo
from math import pi

class TestRectangulo(unittest.TestCase):

    def test_hallarArea(self):
        p= rectangulo(punto(0,0),punto(0,5),punto(10,5),punto(10,0))
        area = p.hallarArea()
        self.assertEquals(area, 50)

    def test_hallarPerimetro(self):
        p= rectangulo(punto(0,0),punto(0,5),punto(10,5),punto(10,0))
        perimetro = p.hallarPerimetro()
        self.assertEquals(perimetro, 30)
        
if __name__ == "__main__":
    unittest.main()