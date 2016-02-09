import unittest
from middleground.read import Read

class TestXls(unittest.TestCase):
    def test_xlsx_simple(self):
        testF = open("tests/files/test.xlsx", "rb")
        xlsx = Read(content=testF.read())
        testF.close()

        xlsxStr = str(xlsx)
        self.assertEqual(xlsxStr[0:19], "Sheet1\n\thello\tworld")

    def test_xlsx(self):
        xlsx = Read(path="tests/files/test2.xlsx")
        xlsxStr = str(xlsx)
        self.assertEqual(xlsxStr[0:68], "worksheet functions.xlsx\n\nSheet1\n\tCategory\tFunction\tDescription\tNew?")

    def test_xls_simple(self):
        self.assertEqual(str(Read(path="tests/files/test.xls"))[0:19], 'Sheet1\n\thello\tworld')

    def test_xls(self):
        xls = Read(path="tests/files/test2.xls")
        xlsStr = str(xls)
        self.assertEqual(xlsStr[0:42], "Sheet1\n\tID\tPoint\tStrain\tsex\tsex#\tage\tbodyw")


if __name__ == '__main__':
    unittest.main()
