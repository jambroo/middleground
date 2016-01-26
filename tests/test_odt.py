import unittest
from middleground.odt import Odt
import os

class TestOdt(unittest.TestCase):
    def test_odt(self):
        pdf = None
        with open("tests/test.odt", 'rb') as odtF:
            odtRaw = odtF.read()
            odt = Odt(odtRaw)
        self.assertEqual(str(odt), "Test Odt!")

if __name__ == '__main__':
    unittest.main()
