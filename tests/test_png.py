import unittest
from middleground.read import Read

class TestPng(unittest.TestCase):
    def test_png(self):
        png = Read(path="tests/files/test.png")
        pngStr = str(png)
        self.assertTrue("BRISBANE" in pngStr)


if __name__ == '__main__':
    unittest.main()
