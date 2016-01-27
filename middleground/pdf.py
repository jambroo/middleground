import tempfile
import os
import io

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.pdfdevice import TagExtractor
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from pdfminer.utils import set_debug_logging

class Pdf:
    def __init__(self, data):
        # Could use SpooledTemporaryFile here to save the temp file into memory
        # instead of onto the disk of the server.
        outTemp = tempfile.mkstemp()
        outfile = outTemp[1]
        outfp = open(outfile, 'wt')

        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, outfp, laparams=LAParams())

        pdfTemp = tempfile.mkstemp()
        pdfFile = pdfTemp[1]
        pdfFp = open(pdfFile, 'wb')
        pdfFp.write(data)
        pdfFp.close()

        pdfFp = open(pdfFile, 'rb')
        process_pdf(rsrcmgr, device, pdfFp, set())
        pdfFp.close()

        os.unlink(pdfFile)

        outfp.close()
        outfp = open(outfile, 'rt')

        self.data = outfp.read()
        if self.data:
            self.data = self.data.strip()

        outfp.close()
        os.unlink(outfile)

    def __str__(self):
        return self.data
