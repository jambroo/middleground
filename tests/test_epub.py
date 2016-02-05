import unittest
from middleground.read import Read


class TestEpub(unittest.TestCase):
    def test_epub(self):
        read = Read(path="tests/files/test.epub")
        self.assertEqual(str(read)[0:33], "Chapter V -- Beyond Good and Evil")


if __name__ == '__main__':
    unittest.main()
