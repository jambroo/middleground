import unittest
from middleground.read import Read


class TestHtml(unittest.TestCase):
    def test_html(self):
        read = Read(path="tests/files/test.html")
        self.assertEqual(str(read), "Hello, world")

    def test_json(self):
        read = Read(path="tests/files/test.json")
        self.assertEqual(str(read), "Hello, world")


if __name__ == '__main__':
    unittest.main()
