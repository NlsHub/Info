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

    return pi

print(approximationPi(15))

#Exercice 5:

def decimalBinaire():