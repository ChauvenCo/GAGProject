from GameLibrary import GameLibrary
from StoreLibrary import StoreLibrary

menuOption = ""

while menuOption != "3":
    print("Bonjour user, veuillez choisir une option parmis les suivantes :")
    print("1 - Bibliothèque locale")
    print("2 - Magasin pas en ligne")
    print("3 - Quitter")

    menuOption = input("Réponse (entre 1 et 3) : ")
    print("\n", end='')

    if menuOption == "1":
        localLibrary = GameLibrary()
        localLibrary.menu()

    if menuOption == "2":
        storeLibrary = StoreLibrary()
        storeLibrary.menu()
