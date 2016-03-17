import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestPs(unittest.TestCase):
    def test_ps(self):
        # WIP
        pass
    #     read = Read(path="tests/files/test.ps")
    #     self.assertEqual(str(read), 'Test')



if __name__ == '__main__':
    unittest.main()
