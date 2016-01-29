import unittest
from middleground.read import Read


class TestPpt(unittest.TestCase):
    def test_ppt(self):
        read = Read(path="tests/files/test.ppt")
        self.assertEqual(str(read)[0:20], "Test PowerPoint FIle")


    def test_pptx(self):
        read = Read(path="tests/files/test.pptx")
        self.assertEqual(str(read)[0:34], "PowerPoint Presentation\n\n\nUTK Quiz")


if __name__ == '__main__':
    unittest.main()
