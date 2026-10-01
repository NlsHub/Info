# Exercice 1:

class Product:

    def __init__(self, code: str, name: str, price: float):
        self.code = code
        self.name = name
        self.price = price


    def get_price_it(self, taxe: float = 0.20):
        return self.price * (1 + taxe)

    def afficheProducts(nombreProduct : int):
        for i in range(nombreProduct) :
            nomProduit = str(input("Donnez le nom d'un produit : "))
            prixTTC = float(input("Combien coute-t-il ? : "))
            codeProduit = str(input("Quel est le code de cet article ? : "))
            produit = Product(codeProduit, nomProduit.upper(), prixTTC)

            print(f"{produit.code} - {produit.name} - {produit.get_price_it()}€")
    
