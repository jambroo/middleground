import json

class Json:
    def __init__(self, data):
        self.data = json.loads(data)

    def __str__(self):
        # TODO: Remove JSON structural characters
        return str(self.data)
