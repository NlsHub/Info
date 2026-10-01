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