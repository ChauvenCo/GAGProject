from GameLibrary import GameLibrary
import json
import os

gameList = []

file = open('Library.json', mode='r')
jsonFile = json.loads(file.read())
file.close()

print("Bonjour user, veuillez choisir une option parmis les suivantes :")
print("1 - Afficher la liste des jeux")

option = input("Réponse (entre 1 et 1) : ")
print("\n")

if option == "1":
    print("Liste des jeux : ")
    gameLibrary = GameLibrary()

    gameList = gameLibrary.getGameList()

    index = 1
    for game in gameList:
        print(str(index), game.nom)
        index += 1

    option = input("Réponse (entre 1 et " + str(index) + ") : ")
    print("\n")

    gameList[int(option) - 1].printDetails()