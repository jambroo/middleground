import html2text

class Html:
    def __init__(self, data):
        self.data = ""
        if data != None and data != "":
            h = html2text.HTML2Text()
            h.ignore_links = True
            self.data = h.handle(data).strip()

    def __str__(self):
        return self.data
