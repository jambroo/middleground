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

    def test_odt2(self):
        pdf = None
        with open("tests/test2.odt", 'rb') as odtF:
            odtRaw = odtF.read()
            odt = Odt(odtRaw)
        self.assertTrue("This appendix is based on Appendix B of Getting Started with OpenOffice.org." in str(odt))

if __name__ == '__main__':
    unittest.main()
