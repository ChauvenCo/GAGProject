class Game:
    def __init__(self, nom: str, tag: str, image: str, prix: float, comments):
        self.nom = nom
        self.tag = tag
        self.image = image
        self.prix = prix
        self.comments = comments

    def __repr__(self):
        returnValue = "Le jeu " + self.tag + "#" + self.nom + " a une image dans : " + self.image + " et est vendu " + str(self.prix) + "€"
        for comment in self.comments:
            returnValue += "\n - " + str(comment)
        return returnValue

    def __eq__(self, other):
        return self.tag == other.tag

    def __hash__(self):
        return hash(self.tag)

    def addComment(self, comment):
        self.comments.append(comment)


class Comments:
    def __init__(self, comment: str):
        self.comment = comment

    def __repr__(self):
        print(self.comment)