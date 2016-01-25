import html2text

class Html:
    def __init__(self, data):
        if data == None or data == "":
            self.data = ""
        else:
            h = html2text.HTML2Text()
            h.ignore_links = True
            self.data = h.handle(data).strip()

    def __str__(self):
        return self.data
