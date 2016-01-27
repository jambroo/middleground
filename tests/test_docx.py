import unittest
from middleground.docx import Docx, Doc

class TestDocx(unittest.TestCase):
    def test_xlsx(self):
        testF = open("tests/files/test2.docx", "rb")
        docx = Docx(testF.read())
        testF.close()

        docxStr = str(docx)
        self.assertEqual(docxStr[0:40], "Description\tTitle of Invention : Sample ")


if __name__ == '__main__':
    unittest.main()
