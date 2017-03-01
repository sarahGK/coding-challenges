import unittest
from evaluation import evaluate

# --- DESCRIPTION --- #
__author__ = 'Xin G Kelly'

# This is the unittest class for the evaluate function
# add test cases under the test method

class EvaluationTestCase(unittest.TestCase):

  def test(self):

    self.assertTrue(evaluate('1') == 1)
    self.assertTrue(evaluate('(1.0)') == 1.0)
    self.assertTrue(evaluate('1+2') == 3)
    self.assertTrue(evaluate('1-2') == -1)
    self.assertTrue(evaluate('1*2') == 2)
    self.assertTrue(evaluate('1/2') == 0.5)
    self.assertTrue(evaluate('2*(1+3)') == 8)
    self.assertTrue(evaluate('1+2-3*4/5') == 1+2-3.0*4.0/5.0)
    self.assertTrue(evaluate('1+2-3*4/(5-7)') == 9)
    self.assertTrue(evaluate('2*(3+(4+(5*6+7)*8))-1') == 2*(3+(4+(5*6+7)*8))-1)
    self.assertTrue(evaluate('100/(((1*2+3)/4-5)+6)') == 100/(((1*2+3)/4-5)+6))

if __name__ == '__main__':
  unittest.main()
