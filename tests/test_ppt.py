import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestPpt(unittest.TestCase):
    def test_ppt(self):
        read = Read(path="tests/files/test.ppt", tikaServer=TIKA_SERVER)
        self.assertEqual(str(read)[0:20], "Test PowerPoint FIle")


    def test_pptx(self):
        read = Read(path="tests/files/test.pptx", tikaServer=TIKA_SERVER)
        self.assertEqual(str(read)[0:34], "PowerPoint Presentation\n\n\nUTK Quiz")


if __name__ == '__main__':
    unittest.main()
