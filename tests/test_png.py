import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestPng(unittest.TestCase):
    def test_png(self):
        png = Read(path="tests/files/meta.png", tikaServer=TIKA_SERVER)
        pngStr = str(png)
        self.assertTrue("BRISBANE" in pngStr)


if __name__ == '__main__':
    unittest.main()
