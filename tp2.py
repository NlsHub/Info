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
classDict["class"]["student"][1]["average"] = sum(ted_marks) / len(ted_marks)
totalAverages = classDict["class"]["student"][0]["average"] + classDict["class"]["student"][1]["average"]
classDict["class"]["average_grade"] = total_averages / len(classDict["class"]["student"])
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