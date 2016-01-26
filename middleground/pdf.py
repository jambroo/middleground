import tempfile
import io

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfdevice import TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.utils import set_debug_logging

#
#     for fname in args:
#         fp = io.open(fname, 'rb')
#         process_pdf(rsrcmgr, device, fp, pagenos, maxpages=maxpages, password=password,
#                     caching=caching, check_extractable=True)
#         fp.close()
#     device.close()
#     if close_outfp:
#         outfp.close()

class Pdf:
    def __init__(self, data):
        rsrcmgr = PDFResourceManager()
        outfp = tempfile.NamedTemporaryFile()
        outfile = outfp.name
        codec = 'utf-8'
        outfp = io.open(outfile, 'wt', encoding=codec, errors='ignore')
        laparams = LAParams()
        device = TextConverter(rsrcmgr, outfp, laparams=laparams)

        t = tempfile.NamedTemporaryFile()
        t.write(data)

        pagenos = set()
        process_pdf(rsrcmgr, device, t, pagenos)
        #
        #
        # print(t.name)
        # doc = PdfReader("tests/test.pdf")
        #
        # print(doc)

        t.close()
        print(outftp)
        outfp.close()

        self.data = ""

    def __str__(self):
        return self.data
