import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestEml(unittest.TestCase):
    def test_eml(self):
        read = Read(path="tests/files/test.eml", tikaServer=TIKA_SERVER)
        self.assertEqual(str(read)[0:4], 'Test')


if __name__ == '__main__':
    unittest.main()
