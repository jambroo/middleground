import unittest
from middleground.read import Read
from test_config import TIKA_SERVER

class TestDocx(unittest.TestCase):
    def test_docx_simple_path(self):
        path = "tests/files/test.docx"
        read = Read(path=path, tikaServer=TIKA_SERVER)
        self.assertEqual(str(read), "Hello world")

    def test_docx_simple_content(self):
        testF = open("tests/files/test.docx", "rb")
        read = Read(content=testF.read(), tikaServer=TIKA_SERVER)
        testF.close()
        self.assertEqual(str(read), "Hello world")

    def test_docx(self):
        testF = open("tests/files/test2.docx", "rb")
        read = Read(content=testF.read(), tikaServer=TIKA_SERVER)
        testF.close()
        self.assertEqual(str(read)[0:29], '12\nEnglish\t\t\t\t\t\t\t\t\t\t\tDrawings')

    def test_doc_simple(self):
        testF = open("tests/files/test.doc", "rb")
        read = Read(content=testF.read(), tikaServer=TIKA_SERVER)
        testF.close()
        self.assertEqual(str(read), "Hello world")

    def test_doc(self):
        testF = open("tests/files/test2.doc", "rb")
        read = Read(content=testF.read(), tikaServer=TIKA_SERVER)
        testF.close()
        self.assertEqual(str(read)[0:36], 'Sample document created with MS Word')

    def test_docx2(self):
        testF = open("tests/files/test3.docx", "rb")
        read = Read(content=testF.read(), tikaServer=TIKA_SERVER)
        testF.close()
        fileContent = str(read)
        contentsSplit = fileContent.split("\n")
        self.assertTrue("Opgaveark:" in contentsSplit[0])
        self.assertEqual(contentsSplit[len(contentsSplit)-1], 'Teknik og Miljø')


if __name__ == '__main__':
    unittest.main()
