class Game:
    def __init__(self, nom: str, tag: str, image: str):
        self.nom = nom
        self.tag = tag
        self.image = image

    def printDetails(self):
        print("Le jeu " + self.tag + "#" + self.nom + " a une image dans : " + self.image)

    def verifyTag(self, tag: str):
        if self.tag == tag:
            return True
        else:
            return False