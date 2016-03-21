import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestRtf(unittest.TestCase):
    def test_tf(self):
        read = Read(path="tests/files/test.rtf", tikaServer=TIKA_SERVER)
        self.assertEqual(str(read)[0:18], "This is a test RTF")


if __name__ == '__main__':
    unittest.main()
