import unittest
from middleground.pdf import Pdf

class TestPdf(unittest.TestCase):
    def test_pdf(self):
        pdf = None
        with open("tests/files/test.pdf", 'rb') as pdfF:
            pdfRaw = pdfF.read()
            pdf = Pdf(pdfRaw)
        self.assertEqual(str(pdf), "hello world")

    def test_long_pdf(self):
        pdf = None
        with open("tests/files/test2.pdf", 'rb') as pdfF:
            pdfRaw = pdfF.read()
            pdf = Pdf(pdfRaw)
        self.assertEqual(str(pdf)[0:14], "Paper 173-2008")

if __name__ == '__main__':
    unittest.main()
