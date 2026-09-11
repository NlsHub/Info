#Exercice 1:

def imc():
    taille = float(input("Donnez votre taille (en mètre) : "))
    poids = float(input("Donnez votre poids (en kilogramme) : "))

    print(poids/(taille**2))

#Exercice 2:

def nEntier():
    listeEntier = [] 
    n = 0
    moyenne = 0
    while n >= 0 :
        n = int(input("Donnez un nombre entier : "))
        if n >= 0 :
            listeEntier.append(n)
    
    for i in range(len(listeEntier)):
        moyenne += listeEntier[i]
        for j in range(i, len(listeEntier)):
            if listeEntier[i] > listeEntier[j] :
                listeEntier[i], listeEntier[j] = listeEntier[j], listeEntier[i]
    print("Nombres trié dans l'ordre croissant : ", listeEntier)
    print("moyenne : ", moyenne/len(listeEntier))
    print("minimum : ", listeEntier[1])
    print("maximum : ", listeEntier[-1])


#Exercice 3:

def conversionAgeChien(age) : 
    assert age > 0, "Vous ne pouvez pas entrer un nombre négatif !"
    age = ((age-1) * 4) + 10.5
    return age

#Exercice 4:

def approximationPi(n):
    assert isinstance(n, int), "n n'est pas un entier"
    assert n > 0, "n n'est pas positif"

    pi = 3
    nb1 = 2
    nb2 = 3
    nb3 = 4

    for i in range(1, n+1):
        if i%2 != 0 :
            pi += 4/(nb1*nb2*nb3)
        else :
            pi -= 4/(nb1*nb2*nb3)
        nb1 += 2
        nb2 += 2
        nb3 += 2

    print(pi)


#Exercice 5:

def decimalBinaire():
    resultat1 = ""
    resultat2 = ""
    q = nombre
    while q != 0 :
        r = q%2
        resultat1 += str(r)
        q = q//2
    for i in range(0, len(resultat1), -1):
        resultat2 += resultat1[i]
    return resultat2

#Exercice 6:

def revisionEx1():

    operation = ""
    operateurDico = {"a" : " + ", "s" : " - ", "m" : " * ", "d" : " / "}
    operateur = str(input("Donnez le type d'opération souhaité ((a)ddition, (s)oustraction, (m)ultiplication et (d)ivision) : "))

    operateur = operateur.lower()

    if operateur not in ["a", "s", "m", "d"] :
        return "Vous n'avez pas donner le type d'opération souhaité"
    
    nb1 = float(input("Donnez un premier nombre à insérer dans le calcul : "))
    nb2 = float(input("Donnez le deuxième nombre à insérer dans le calcul : "))
    assert isinstance(nb1,float ), "Vous n'avez pas entré un entier, la saisie n'est pas correct"
    assert isinstance(nb2, float), "Vous n'avez pas entré un entier, la saisie n'est pas correct"

    continuer = "o"
    while continuer == "o" :
        if operateur == "a" :
            resultat = nb1 + nb2
        elif operateur == "s" :
            resultat = nb1 - nb2
        elif operateur == "m" :
            resultat = nb1 * nb2
        else :
            if nb2 == 0 :
                return "résultat non déterminé : la division par zéro est impossible"
            resultat = nb1 / nb2
        

        operation += str(nb1) + operateurDico[operateur] + str(nb2) + " = " + str(resultat)
        print(operation)
        
        continuer = str(input("un autre calcul ? (o/n) : "))


#Exercice 7:

from string import *
from random import randint

def immatriculation() :
    plaque = ""
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(4):
        indiceLettre = randint(0, 25)
        if alphabet[indiceLettre] == "s" and plaque[-1] == "S" :
            while alphabet[indiceLettre] == "s" :
                indiceLettre = randint(0, 26)

        lettre = alphabet[indiceLettre].upper()
        plaque += f"{lettre}"

        if i == 1:
            nombre1 = randint(0, 9)
            nombre2 = randint(0, 9)
            nombre3 = randint(0, 9)
            plaque += f"-{nombre1}{nombre2}{nombre3}-"

    print(plaque)

#______________________________________________________________________DLC_______________________________________________________________

#Exercice 1:

def main(nbExo = 0):


    repete = True

    while repete == True :
        print("Quel exercice voulez-vous voir ?")
        print(" - 1 : IMC\n - 2 : Année Chien\n - 3 : Les n entiers\n - 4 : Valeur Pi\n - 5 : Transformation en binaire\n - 6 : Révision exercice 1\n - 7 : Plaque d'immatriculation")
        nbExo = int(input())
        if nbExo == 1 :
            print(imc())
        elif nbExo == 2:
            age = int(input("Donner l'age à transformer : ")) 
            print(conversionAgeChien(age))
        elif nbExo == 3:
            print(nEntier())
        elif nbExo == 4:
            approximation = int(input("Donner le nombre d'approximation de pi : ")) 
            print(conversionAgeChien(approximation))
        elif nbExo == 5:
            nbTransfo = int(input("Donner un nombre à transformer : ")) 
            print(decimalBinaire(nbTransfo))
        elif nbExo == 6:
            print(revisionEx1())
        else :
            print(plaqueImmatriculation())

        autreExo = str(input("Voulez-vous voir un autre exercice ? (o/n) :  "))
        if autreExo != "o" :
            repete = False

print(main())

#Exercice 2:

def fizzBuzz(liste):
    for i in range(len(liste)):
        if liste[i]%3 == 0 and liste[i]%5 != 0:
            print("Fizz", end = ' ')
        elif liste[i]%5 == 0 and liste[i]%3 != 0:
            print("Buzz", end = ' ')
        elif liste[i]%5 == 0 and liste[i]%3 == 0:
            print("Fizzbuzz", end = ' ')
        else :
            print(liste[i], end = ' ')

fizzBuzz([5,8,7,4,1,3,6,9,5])

#Exercice 3:

def jeuDeCarte():
    couleur = ["♠", "♣", "♦", "♥"]
    valeur = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "V", "D", "R", "1"]
    
    pointsOrdi = 0
    pointsJoueur = 0

    paquetCartes = {}

    for i in range(len(valeur)):
            paquetCartes[valeur[i]] = couleur

    recommencer = "o"

    while recommencer == "o" :
        
        valeurPiochee = randint(0, 12)
        couleurPiochee = randint(0, len(paquetCartes[cartePiochee]))
        print(paquetCartes[cartePiochee][couleurPiochee])
        paquetCartes.pop(paquetCartes[cartePiochee][couleurPiochee])

        for i in range(10):
            prediction = str(input("Pensez-vous que la prochaine carte sera supérieure(s) ou inférieure(i) à cette carte ? : "))
            valeurPiochee = randint(0, 12)
            couleurPiochee = randint(0, len(paquetCartes[cartePiochee]))
            print(paquetCartes[cartePiochee][couleurPiochee])
            paquetCartes.pop(paquetCartes[cartePiochee][couleurPiochee])
            

