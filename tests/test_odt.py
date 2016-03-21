import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestOdt(unittest.TestCase):
    def test_odt(self):
        pdf = None
        with open("tests/files/test.odt", 'rb') as odtF:
            odtRaw = odtF.read()
            odt = Read(content=odtRaw, tikaServer=TIKA_SERVER)
        self.assertEqual(str(odt), "Test Odt!")

    def test_odt2(self):
        odt = Read(path="tests/files/test2.odt", tikaServer=TIKA_SERVER)
        self.assertTrue("This appendix is based on Appendix B of Getting Started with OpenOffice.org." in str(odt))

if __name__ == '__main__':
    unittest.main()
