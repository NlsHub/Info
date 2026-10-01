# Exercice 1:

class Product:

    def __init__(self, code: str, name: str, price: float):
        self.code = code
        self.name = name
        self.price = price
        taxe = 0.20


    def get_price_it(self, taxe: float):
        return self.price * (1 + taxe)

    def afficheProducts(nombreProduct : int):
        for i in range(nombreProduct) :
            nomProduit = str(input("Donnez le nom d'un produit : "))
            prixTTC = float(input("Combien coute-t-il ? : "))
            codeProduit = str(input("Quel est le code de cet article ? : "))
            produit = Product(codeProduit, nomProduit.upper(), prixTTC)

            print(f"{produit.code} - {produit.name} - {produit.get_price_it()}€")
    
#Exercice 2:

class Fraction:

    def __init__(self, numerateur : int, denominateur : int):
        self.numerateur = numerateur
        self.denominateur = denominateur
    
    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"
    
    def __sub__(self, other):
        if self.denominateur != other.denominateur :
            num = (self.numerateur * other.denominateur) + (other.numerateur * self.denominateur)
            den = self.denominateur * other.denominateur
        else :
            num = self.numerateur + other.numerateur
            den = self.denominateur
            
        return Fraction(num, den)

    def __sub__(self, other):
        if self.denominateur != other.denominateur :
            num = (self.numerateur * other.denominateur) - (other.numerateur * self.denominateur)
            den = self.denominateur * other.denominateur
        else :
            num = self.numerateur - other.numerateur
            den = self.denominateur

        return Fraction(num, den)

    def __mul__(self, other):
        num = self.numerateur  * other.numerateur 
        den = self.denominateur * other.denominateur
        
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.numerateur  * other.denominateur
        den = self.denominateur * other.numerateur
        
        return Fraction(num, den)

    def __lt__(self, other):
        return (self.numerateur/self.denominateur) < (other.numerateur/other.denominateur)

    def __gt__(self, other):
        return (self.numerateur/self.denominateur) > (other.numerateur/other.denominateur)

    def __le__(self, other):
        return (self.numerateur/self.denominateur) <= (other.numerateur/other.denominateur)

    def __ge__(self, other):
        return (self.numerateur/self.denominateur) >= (other.numerateur/other.denominateur)

    def __eq__(self, other):
        return (self.numerateur/self.denominateur) == (other.numerateur/other.denominateur)

    def __ne__(self, other):
        return (self.numerateur/self.denominateur) != (other.numerateur/other.denominateur)


#Exercice 3:
#♠︎♥︎♦︎♣︎

import sys
from random import shuffle

class CardValue :
    def __init__(self, value_txt, value_pts):
        self.value_txt = value_txt
        self.value_pts = value_pts


class CardColor :
    def __init__(self, shade, shade_name, foreground_color, background_color):
        self.shade = shade
        self.shade_name = shade_name
        self.foreground_color = foreground_color
        self.background_color = background_color


class Card :
    def __init__(self, value, color):
        self.value = CardValue(*value)
        self.color = CardColor(*color)

    def is_equal_value(self, card):
        return self.value.value_pts == card.value.value_pts

def __str__(self):
    return (
        f"Valeur : {self.value.value_txt} ({self.value.value_pts} pts) | "
        f"Couleur : {self.color.shade} {self.color.shade_name} | "
        f"Style : {self.color.foreground_color}/{self.color.background_color}"
    )

    def __repr__(self):
        return f"Card('{self.value.value_txt}', '{self.color.shade_name}')"

class Deck :
    def __init__(self, deck, defausse):
        self.deck = []
        self.defausse = []
        self.init52_cards()

    def init52_cards(self):
        valeurs = [
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("V", 11),
            ("D", 12),
            ("R", 13),
            ("A", 14),
        ]

        couleurs = [
        ("♠︎", "pique", "noir", "blanc"),
        ("♣︎", "trèfle", "noir", "blanc"),
        ("♥︎", "cœur", "rouge", "blanc"),
        ("♦︎", "carreau", "rouge", "blanc"),
    ]

    self.deck = [Card(val, coul) for coul in couleurs for val in valeurs]

    def shuffle(self):
        shuffle(self.deck)
    
    def draw(self):
        if not self.deck:
            return None
        return self.deck.pop(0)

    def discard(self, card):
        self.defausse.append(card)

carte1 = Card(("10", 10), ("♠︎", "pique", "noir", "blanc"))
carte2 = Card(("10", 10), ("♥︎", "coeur", "rouge", "blanc"))
carte3 = Card(("9", 9), ("♦︎", "carreau", "rouge", "blanc"))

print(carte1)
print(repr(carte1))

mon_deck = Deck()
print(mon_deck)

mon_deck.Shuffle()

carte_tiree = mon_deck.Draw()
print(f"Carte piochée : {carte_tiree}")

mon_deck.Discard(carte_tiree)

print(mon_deck)
