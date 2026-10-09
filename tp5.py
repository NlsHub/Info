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

#Exercice 2:

class Airplane :
    def __init__(self, name : str):
        assert isinstance(name, str)
        self.name = name
        self.fly = False
    
    def take_off(self):
        self.fly = True
    
    def land(self):
        self.fly = False

    def __str__(self):
        etat = "en vol" if self.fly else "au sol"
        print(f"Nom de l'avion : {self.name} \n Etat : {etat}")


class MilitaryAircraft(Airplane) :
    def __init__(self, name):
        super().__init__(name)
        self.mission = ""
    
    def __str__(self):
        etat = "en vol" if self.fly else "au sol"
        print(f"Nom de l'avion : {self.name} \n Etat : {etat}\n Mission : {self.mission}")

class CargoAircraft(Airplane) :
    def __init__(self, name):
        super().__init__(name)
        self.shipment = ""

    def __str__(self):
        etat = "en vol" if self.fly else "au sol"
        print(f"Nom de l'avion : {self.name} \n Etat : {etat}\n Cargaison : {self.shipment}")


class CivilAircraft(Airplane) : 
    def __init__(self, name):
        super().__init__(name)
        self.nbPassager = 0

    def passenger_enter(nb : int):
        self.nbPassager += nb 

    def passenger_leave(nb : int):
        if (self.nbPassager-nb) >= 0 :     
            self.nbPassager -= nb 

    def __str__(self):
        etat = "en vol" if self.fly else "au sol"
        print(f"Nom de l'avion : {self.name} \n Etat : {"en vol" if self.fly == True else "au sol"} \n Nombre de passagers : {self.nbPassager}")

class Airport(MilitaryAircraft, CivilAircraft, CargoAircraft) :
    
    def __init__(self):
        super()__init__(self)

    def add_military(self, plane : MilitaryAircraft):
    
    def add_cargo(self, plane : CargoAircraft):

    def add_civil(self, plane : CivilAircraft):