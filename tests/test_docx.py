import unittest
from middleground.read import Read
import config

class TestDocx(unittest.TestCase):
    def test_docx_simple_path(self):
        path = "tests/files/test.docx"
        read = Read(path=path)
        self.assertEqual(str(read), "Hello world")

    def test_docx_simple_content(self):
        testF = open("tests/files/test.docx", "rb")
        read = Read(content=testF.read())
        testF.close()
        self.assertEqual(str(read), "Hello world")

    def test_docx(self):
        testF = open("tests/files/test2.docx", "rb")
        read = Read(content=testF.read())
        testF.close()
        self.assertEqual(str(read)[0:29], '12\nEnglish\t\t\t\t\t\t\t\t\t\t\tDrawings')

    def test_doc_simple(self):
        testF = open("tests/files/test.doc", "rb")
        read = Read(content=testF.read())
        testF.close()
        self.assertEqual(str(read), "Hello world")

    def test_doc(self):
        testF = open("tests/files/test2.doc", "rb")
        read = Read(content=testF.read())
        testF.close()
        self.assertEqual(str(read)[0:36], 'Sample document created with MS Word')


if __name__ == '__main__':
    unittest.main()