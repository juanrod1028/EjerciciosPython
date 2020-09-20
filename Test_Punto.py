import unittest
from Punto import punto

class TestPunto(unittest.TestCase):

    def test_hallarDistancia(self):
        p = punto(1,0) 
        p2 = punto(-1,0)
        distancia = p.hallarDistancia(p2)
        self.assertEquals(distancia, 2)
        
if __name__ == "__main__":
    unittest.main()