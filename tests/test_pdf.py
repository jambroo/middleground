import unittest
from middleground.read import Read

class TestPdf(unittest.TestCase):
    def test_pdf(self):
        pdf = None
        with open("tests/files/test.pdf", 'rb') as pdfF:
            pdfRaw = pdfF.read()
            pdf = Read(content=pdfRaw)
        self.assertEqual(str(pdf), "hello world")

    def test_long_pdf(self):
        pdf = Read(path="tests/files/test2.pdf")
        self.assertEqual(str(pdf)[0:18], "1 \n\nPaper 173-2008")

if __name__ == '__main__':
    unittest.main()
