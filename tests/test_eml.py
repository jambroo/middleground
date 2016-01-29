import unittest
from middleground.read import Read
import config

class TestEml(unittest.TestCase):
    def test_eml(self):
        read = Read(path="tests/files/test.eml")
        self.assertEqual(str(read)[0:4], 'Test')


if __name__ == '__main__':
    unittest.main()
