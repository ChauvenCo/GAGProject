from GameManager import GameManager
from Game import Game


class StoreLibrary(GameManager):
    def __init__(self):
        super().__init__("StoreLibrary.json", True)

    def buyGame(self, game: Game, localLibraryPath: str):
        manager = GameManager(localLibraryPath, False)
        oldLen = len(manager.gameLibrary)
        manager.addGame(game.nom, game.tag, game.image, game.prix)
        return oldLen != len(manager.gameLibrary)

    def menu(self):
        menuOption = 0
        while menuOption != 5:
            print("Que voulez-vous faire :")
            print("1 - Jeux sur le marché")
            print("2 - Acheter un jeu")
            print("3 - Ajouter un commentaire")
            print("4 - Pleurer")
            print("5 - Quitter")

            menuOption = int(input("Réponse (entre 1 et 4) : "))
            print("\n", end='')

            if menuOption < 4:
                print("Liste des jeux du magasin : ")

                gamechoice = 0
                index = 1
                while gamechoice != str(index):
                    index = 1
                    for game in self.gameLibrary:
                        print(str(index), game.nom)
                        index += 1
                    print(str(index), "Retour")

                    gamechoice = input("Réponse (entre 1 et " + str(index) + ") : ")

                    if gamechoice != str(index):
                        print("\n", end='')

                        if menuOption == 1:
                            print(list(self.gameLibrary)[int(gamechoice) - 1])
                        elif menuOption == 2:
                            if self.buyGame(list(self.gameLibrary)[int(gamechoice) - 1], "LocalLibrary.json"):
                                print("Jeu acheté")
                            else:
                                print("Jeu déjà acheté. Arrêtez de nous donner votre argent pour rien !")
                        elif menuOption == 3:
                            comment = input("Quel est votre commentaire : ")
                            for item in self.gameLibrary:
                                if item == list(self.gameLibrary)[int(gamechoice) - 1]:
                                    item.addComment(comment)
                            self.actualise()

                    print("\n", end='')

            if menuOption == 4:
                print("Bah oui t'as pas d'argent...")
                print("\n", end='')