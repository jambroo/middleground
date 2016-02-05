import unittest
from middleground.read import Read
import config

class TestMsg(unittest.TestCase):
    def test_msg(self):
        read = Read(path="tests/files/test.msg")
        self.assertEqual(str(read).find("Dear BitDaddys Corp"), 212)


if __name__ == '__main__':
    unittest.main()
