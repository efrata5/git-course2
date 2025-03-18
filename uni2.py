import unittest
import unit1
class TestCap(unittest.TestCase):
   def test_one_word(self):
      text='python'
      result=unit1.cap_text(text)
      self.assertEqual(result,'Python')
   def test_multiple_word(self):
      text='month'
      result=unit1.cap_text(text)
      self.assertEqual(result,'Month')
if __name__=='__main__':
   unittest.main()