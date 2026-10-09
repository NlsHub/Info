#Exercice 1:

class Rectangle :

    def __init__(self, longueur, largeur):
        self.largeur = largeur
        self.longueur = longueur
        self.nom = "rectangle"

    def surface(self):
        return self.longueur * self.largeur

    def affichage(self):
        print(f"c'est un {self.nom} de surface {self.surface()} cm²")

class Carre(Rectangle) : 
    def __init__(self, cote):
        super().__init__(longueur = cote, largeur = cote)
        self.nom = "carré"

rectangle = Rectangle(10, 2)
carre = Carre(10)

rectangle.affichage()
carre.affichage()