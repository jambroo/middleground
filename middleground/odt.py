from odf.odf2xhtml import ODF2XHTML
from .html import Html
import tempfile

class Odt:
    def __init__(self, data):
        t = tempfile.NamedTemporaryFile()
        t.write(data)

        odhandler = ODF2XHTML(False, False)
        result = odhandler.odf2xhtml(t.name)
        self.data = str(Html(result))

        t.close()

    def __str__(self):
        return self.data
