import docx

import tempfile
import os

class Doc:
    def __init__(self, data):
        outTemp = tempfile.mkstemp(suffix=self.get_extension())
        outfile = outTemp[1]
        outfp = open(outfile, 'wb')
        outfp.write(data)
        outfp.close()

        document = docx.opendocx(outfile)
        text = docx.getdocumenttext(document)
        self.data = ""
        if type(text) == list:
            self.data = "\t".join(text)

        os.unlink(outfile)

    def get_extension(self):
        return "doc"

    def __str__(self):
        return self.data


class Docx(Doc):
    def get_extension(self):
        return "docx"
