import radiation
import unittest
from unittest.loader import defaultTestLoader
from matplotlib.mathtext import DELTA
class firstTestCase(unittest.TestCase):
    
    def test_findFlow(self):
        self.assertAlmostEqual(radiation.findFlow(0.8,300, 1.0),367.4,places=None,delta = 0.1)
    def test_findEpsilon(self):
        self.assertAlmostEqual(radiation.findEpsilon(367.4, 300, 1.0),0.8,places=None,delta = 0.1)
    def test_findT(self):
        self.assertAlmostEqual(radiation.findT(367.4, 0.8, 1.0),300,places=None,delta = 0.1)
    def test_findA(self):
        self.assertAlmostEqual(radiation.findA(367.4, 0.8, 300),1.0,places=None,delta = 0.1)
def suite_use_make_suite():
    s = unittest.TestSuite
    s.addTest(firstTestCase)

if __name__ == '__main__':
    unittest.main()