import unittest
from middleground.read import Read
import config

class TestRead(unittest.TestCase):
    def test_read(self):
        with self.assertRaises(Exception) as cm:
            read = Read()

        self.assertEqual(str(cm.exception), "A path to the file or the content of the file must be provided.")


if __name__ == '__main__':
    unittest.main()
