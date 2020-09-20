import unittest
from Punto import punto
from Circulo import circulo
from math import pi

class TestCirculo(unittest.TestCase):

    def test_hallarArea(self):
        c = circulo(1,punto(0,0))
        area = c.hallarArea()
        self.assertEquals(area, pi)

    def test_hallarPerimetro(self):
        c = circulo(1,punto(0,0))
        perimetro = c.hallarPerimetro()
        self.assertEquals(perimetro, 2*pi)

    def test_determinarPuntoDentro(self):
        p = punto(8,0)
        c = circulo(3,punto(10,0))
        d = c.determinarPuntoDentro(p)
        self.assertTrue(d)
        
if __name__ == "__main__":
    unittest.main()