import unittest
from middleground.pdf import Pdf

class TestPdf(unittest.TestCase):
    def test_pdf(self):
        pdf = None
        with open("tests/test.pdf", 'rb') as pdfF:
            pdfRaw = pdfF.read()
            pdf = Pdf(pdfRaw)
        self.assertEqual(str(pdf), "hello world")

if __name__ == '__main__':
    unittest.main()
