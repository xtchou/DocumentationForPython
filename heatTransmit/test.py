import heatTransmit
import unittest

class firstTestCase(unittest.TestCase):
    
    def test_findFlow(self):
        self.assertAlmostEqual(heatTransmit.findP(49.33, 3.14*0.014*80/1000, 49),8.5,places=None,delta = 0.1)
    def test_findEpsilon(self):
        self.assertAlmostEqual(heatTransmit.findH(8.5,3.14*0.014*80/1000 , 49),49.33,places=None,delta = 0.1)
    def test_findT(self):
        self.assertAlmostEqual(heatTransmit.findA(8.5, 49.33, 49),3.14*0.014*80/1000,places=None,delta = 0.1)
    def test_findA(self):
        self.assertAlmostEqual(heatTransmit.findDt(8.5, 49.33, 3.14*0.014*80/1000),49,places=None,delta = 0.1)
def suite_use_make_suite():
    s = unittest.TestSuite
    s.addTest(firstTestCase)

if __name__ == '__main__':
    unittest.main()