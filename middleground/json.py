import json

class Json:
    def __init__(self, data):
        self.data = json.loads(data)

    def to_str(self, deserialized_json):
        out = ""
        if isinstance(deserialized_json, dict):
            for key in sorted(deserialized_json):
                print(key)
                out += self.to_str(deserialized_json[key]) + " "
            return out

        if isinstance(deserialized_json, list):
            for item in deserialized_json:
                out += self.to_str(item) + " "
            return out

        if isinstance(deserialized_json, str):
            return deserialized_json
        else:
            return ""

    def __str__(self):
        return self.to_str(self.data)
