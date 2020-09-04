import unittest
import Problema3

class TestProblema3(unittest.TestCase):

    def test_caracter(self):
        letras= Problema3.caracter("hola")
        self.assertEquals(letras, ['h','a'])
        
if __name__ == "__main__":
    unittest.main()