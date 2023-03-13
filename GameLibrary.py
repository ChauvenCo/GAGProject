from JsonManager import JsonManager
from Game import Game

class GameLibrary:
    def __init__(self):
        self.json = JsonManager("Library.json")
        self.gameLibrary = []

        for game in self.json.jsonFile["games"]:
            self.gameLibrary.append(Game(game["nom"], game["tag"], game["image"]))

    def deleteGame(self, tag: str):
        for i in range(0, len(self.gameLibrary) - 1):
            if self.gameLibrary[i].verifyTag(tag):
                del self.gameLibrary[i]
                break

    def getGameList(self):
        return self.gameLibrary

    def addGame(self, nom: str, tag: str, image: str):
        alreadyExist = False

        for i in range(0, len(self.gameLibrary) - 1):
            if self.gameLibrary[i].verifyTag(tag):
                print("Ce jeu existe déjà. Tag : ", tag)
                alreadyExist = True

        if not alreadyExist:
            self.gameLibrary.append(Game(nom, tag, image))
