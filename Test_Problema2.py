import unittest
import Problema2 

class TestProblema2(unittest.TestCase):

    def test_parImpar(self):
        verificar = Problema2.parImpar(5)
        self.assertTrue(verificar)

if __name__ == "__main__":
    unittest.main()