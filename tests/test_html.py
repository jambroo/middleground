import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestHtml(unittest.TestCase):
    def test_html(self):
        read = Read(path="tests/files/test.html", tikaServer=TIKA_SERVER)
        self.assertEqual(str(read), "Hello, world")


if __name__ == '__main__':
    unittest.main()
