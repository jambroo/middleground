from tika import parser

class Read:
    CONVERTED=0
    ALREADY_EXISTS=1
    TYPE_ERROR=2
    UNKNOWN_ERROR=3

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
