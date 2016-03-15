from tika import parser

class Read:
    def __init__(self, path=None, content=None, tikaServer=None):
        if path is not None:
            parsed = parser.from_file(path, tikaServer)
        elif content is not None:
            parsed = parser.from_buffer(content, tikaServer)
        else:
            raise Exception("A path to the file or the content of the file must be provided.")

        self.data = ""
        if parsed["content"]:
            self.data = parsed["content"].strip()

        self.metadata = []
        if "metadata" in parsed:
            self.metadata = parsed


    def __str__(self):
        return self.data
