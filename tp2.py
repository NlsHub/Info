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
    if polynome == []:
        return "0"

    taille = 0
    temp = polynome
    while temp != []:
        taille += 1
        temp = temp[1]

    degre = taille - 1
    affichage = ""

    while polynome != []:
        valeur = polynome[0]

        if degre == 0:
            affichage += f"{valeur}"
        elif degre == 1:
            affichage += f"{valeur}x"
        else:
            affichage += f"{valeur}x^{degre}"

        polynome = polynome[1]

        if polynome != []:
            affichage += " + "

        degre -= 1
        
    return affichage

print(affichagePolynome([5,[6,[8,[3,[]]]]]))

#Exercice 6 :

import requests 

def get_university_data(country = "France"):
    url = f"http://universities.hipolabs.com/search?country={country}"

    rawdata = requests.get(url)

    if not rawdata:
        raise Exception

    data = rawdata.json()
    return data


if __name__ == "__main__":
    uni_data = get_university_data("France")
    print(uni_data)