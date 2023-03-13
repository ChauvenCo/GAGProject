from GameManager import GameManager

class GameLibrary(GameManager):
    def __init__(self):
        super().__init__("LocalLibrary.json", False)

    def menu(self):
        menuOption = 0
        while menuOption != 3:
            print("Que voulez-vous faire :")
            print("1 - Détails des jeux")
            print("2 - Supprimer un jeu")
            print("3 - Quitter")

            menuOption = int(input("Réponse (entre 1 et 3) : "))
            print("\n", end='')

            if menuOption != 3:
                print("Liste des jeux de la bibliothèque locale : ")

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
                            self.deleteGame(list(self.gameLibrary)[int(gamechoice) - 1].tag)
                            print("Jeu supprimé")

                    print("\n", end='')

