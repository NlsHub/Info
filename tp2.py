from random import randint

#TP 2 : Collections

#Exercice 2:

classDict = {
 "class": {
 "student": {
 "name": "Mike",
 "marks": {
 "physics": 70,
 "history": 80
 }
 }
 }
 }

print("Nom de l'étudiant :", classDict["class"]["student"]["name"])
classDict["class"]["student"]["marks"]["physics"] = 89
mikeMarks = classDict["class"]["student"]["marks"].values()
classDict["class"]["student"]["average"] = sum(mikeMarks) / len(mikeMarks)
mikeData = classDict["class"]["student"]
classDict["class"]["student"] = [mikeData]

tedData = {
    "name": "Ted",
    "marks": {
        "physics": 34, 
        "history": 99
    }
}
classDict["class"]["student"].append(tedData)
tedMarks = classDict["class"]["student"][1]["marks"].values()
classDict["class"]["student"][1]["average"] = sum(tedMarks) / len(tedMarks)
totalAverages = classDict["class"]["student"][0]["average"] + classDict["class"]["student"][1]["average"]
classDict["class"]["average_grade"] = totalAverages / len(classDict["class"]["student"])
print(classDict)


#Exercice 3:
n = randint(3, 99)
tab = [randint(0, 500) for i in range(n)]
print(tab)

def differents(tab):
    dico = {}
    for element in tab:
        if element not in dico.keys():
            dico[element] = 1
        else :
            dico[element] += 1
    for element in dico.values() :
        if element != 1 :
            return False
    return True
print(differents(tab))

#Exercice 4:

p = ["10","2","C","D","+"]

def scoreBaseball(p):
    pileScore = []
    for i in range(len(p)):
        if p[i] == "+":
            pileScore.append(pileScore[-1]+pileScore[-2])
        elif p[i] == "D":
            pileScore.append(pileScore[-1]*2)
        elif p[i] == "C":
            pileScore.pop()
        else :
            pileScore.append(int(p[i]))
    return pileScore

print(scoreBaseball(p))

#Exercice 5 :

def ajoutcoef(polynome):
    coef = float(input("Donnez un nouveau coefficient à ajouter : "))
    nouveauPolynome = [coef, polynome]
    return nouveauPolynome

def saisiePolynome():
    polynome = []
    degre = int(input("Quel sera le degré de votre polynôme ? : "))
    for i in range(degre+1): 
        coef = float(input(f"Donnez le coefficient de degré {i} à ajouter : "))
        polynome = [coef, polynome]
    return polynome

def affichagePolynome(polynome):
    affichage = ""
    i = 0
    degre = 0

    polynome1 = polynome

    while polynome1 != [] :
        valeur = polynome[0]
        suivant = polynome[1]
        polynome = suivant
        i += 1
        degre += 1

    if polynome != []:
        affichage += f"{str(valeur)} + "

    while polynome != [] :

        valeur = polynome[0]
        suivant = polynome[1]
        if i == degre-1 :
            affichage += f"{str(valeur)}x + "
        else :
            affichage += f"{str(valeur)}x{i} + "
        polynome = suivant
        i -= 1
    
    return affichage[:-2]

print(affichagePolynome([5,[6,[8,[3,[]]]]]))