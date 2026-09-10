#Exercice 1:

def imc():
    taille = float(input("Donnez votre taille (en mètre) : "))
    poids = float(input("Donnez votre poids (en kilogramme) : "))

    print(poids/(taille**2))

#Exercice 2:

def Nentier():
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

Nentier()