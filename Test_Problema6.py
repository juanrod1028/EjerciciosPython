import unittest
from Problema6 import problema6

class TestProblema1(unittest.TestCase):

    def test_edad2070(self):
        p = problema6() 
        palindromo = p.soyPalindromo("ala")
        self.assertTrue(palindromo)
        
if __name__ == "__main__":
    unittest.main()