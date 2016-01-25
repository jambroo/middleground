import json

class Json:
    def __init__(self, data):
        self.data = json.loads(data)

    def to_str(self, deserialized_json, depth=0):
        out = ""

        if isinstance(deserialized_json, dict):
            for key in sorted(deserialized_json):
                for i in range(0, depth):
                    out += "  "
                out += key + "\n"
                out += self.to_str(deserialized_json[key], depth+1) + "\n"
        elif isinstance(deserialized_json, list):
            for key in range(0, len(deserialized_json)):
                item = deserialized_json[key]
                for i in range(0, depth):
                    out += "  "
                out += str(key) + "\n"
                out += self.to_str(item, depth+1) + "\n"
        elif isinstance(deserialized_json, str):
            for i in range(0, depth):
                out += "  "
            out += deserialized_json

        return out

    def __str__(self):
        return self.to_str(self.data)
