import unittest
from middleground.read import Read


class TestRtf(unittest.TestCase):
    def test_tf(self):
        read = Read(path="tests/files/test.rtf")
        self.assertEqual(str(read)[0:18], "This is a test RTF")


if __name__ == '__main__':
    unittest.main()
