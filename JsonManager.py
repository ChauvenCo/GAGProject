import json

class JsonManager:
    def __init__(self, path: str):
        self.path = path

        file = open(self.path, mode='r')
        self.jsonFile = json.loads(file.read())
        file.close()

    def modifyJson(self, jsonFile):
        self.jsonFile = jsonFile

    def save(self):
        file = open(self.path, mode='w')
        file.write(self.jsonFile)
        file.close()

