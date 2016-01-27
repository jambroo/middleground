import unittest
from middleground.xlsx import Xlsx, Xls

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

    def test_xls_simple(self):
        testF = open("tests/files/test.xls", "rb")
        xls = Xls(testF.read())
        testF.close()

        xlsStr = str(xls)
        self.assertEqual(xlsStr, "hello\tworld")

    def test_xls(self):
        testF = open("tests/files/test2.xls", "rb")
        xls = Xls(testF.read())
        testF.close()

        xlsStr = str(xls)
        self.assertEqual(xlsStr[0:34], "ID\tPoint\tStrain\tsex\tsex#\tage\tbodyw")

if __name__ == '__main__':
    unittest.main()
