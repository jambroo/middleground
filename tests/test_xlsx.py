import unittest
from middleground.xls import Xlsx

class TestXls(unittest.TestCase):
    def test_xlsx_simple(self):
        testF = open("tests/files/test.xlsx", "rb")
        xlsx = Xlsx(testF.read())
        testF.close()

        xlsxStr = str(xlsx)
        self.assertEqual(xlsxStr, "hello\tworld")

    def test_xlsx(self):
        testF = open("tests/files/test2.xlsx", "rb")
        xlsx = Xlsx(testF.read())
        testF.close()

        xlsxStr = str(xlsx)
        self.assertEqual(xlsxStr[0:34], "Category\tFunction\tDescription\tNew?")

if __name__ == '__main__':
    unittest.main()
