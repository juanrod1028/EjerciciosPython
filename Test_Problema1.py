import unittest
import Problema1 

class TestProblema1(unittest.TestCase):

    def test_edad2070(self):
        edad = Problema1.edad2070(15)
        self.assertEquals(edad, 65)
if __name__ == "__main__":
    unittest.main()