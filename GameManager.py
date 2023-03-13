from JsonManager import JsonManager
from Game import Game

class GameManager:
    def __init__(self, path: str, withComment: bool):
        self.json = JsonManager(path)
        self.gameLibrary = set()

        for game in self.json.jsonContent["games"]:
            if withComment:
                self.gameLibrary.add(Game(game["nom"], game["tag"], game["image"], game["prix"], game["comments"].copy()))
            else:
                self.gameLibrary.add(Game(game["nom"], game["tag"], game["image"], game["prix"], []))

    def deleteGame(self, tag: str):
        for i in range(0, len(self.gameLibrary)):
            if list(self.gameLibrary)[i].tag == tag:
                self.gameLibrary.remove(list(self.gameLibrary)[i])
                break
        self.actualise()

    def addGame(self, nom: str, tag: str, image: str, prix: float):
        self.gameLibrary.add(Game(nom, tag, image, prix, []))
        self.actualise()

    def actualise(self):
        self.json.jsonContent["games"].clear()
        for game in self.gameLibrary:
            self.json.jsonContent["games"].append({"nom" : game.nom, "tag" : game.tag, "image" : game.image, "prix" : game.prix, "comments": game.comments})
        self.json.save()
