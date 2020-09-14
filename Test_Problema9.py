import unittest
from Problema9 import problema9

class TestProblema9(unittest.TestCase):

    def test_nDeN(self):
        p= problema9()
        lista = p.nDeN(5)
        self.assertEquals(lista, [5,5,5,5,5])
        
if __name__ == "__main__":
    unittest.main()