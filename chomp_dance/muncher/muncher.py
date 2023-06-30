import json

class Muncher:
    def parse_file(file=None):
        if file is None:
            return FileNotFoundError
        with open(file, encoding="utf-8") as f:
            json_data = f.read()
        if f.closed is False:
            return IOError
        print(json_data)

