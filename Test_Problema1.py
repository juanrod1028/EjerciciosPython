import unittest
from Problema1 import problema1

class TestProblema1(unittest.TestCase):

    def test_edad2070(self):
        p = problema1() 
        edad = p.edad2070(15)
        self.assertEquals(edad, 65)
        
if __name__ == "__main__":
    unittest.main()