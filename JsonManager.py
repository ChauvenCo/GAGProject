import json

class JsonManager:
    def __init__(self, path: str):
        self.path = path

        file = open(self.path, mode='r')
        self.jsonContent = json.loads(file.read())
        file.close()

    def save(self):
        file = open(self.path, mode='w')
        file.write(str(self.jsonContent).replace("'", '"'))
        file.close()

