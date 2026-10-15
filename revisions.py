def decalage_cesar(cle, phrase):
    cle = cle.upper()
    phrase = phrase.upper()
    
    resultat = ""
    n_cle = len(cle)
    
    for i in range(len(phrase)):
        char = phrase[i]
        
        if 'A' <= char <= 'Z':
            decalage = ord(cle[i % n_cle]) - ord('A') + 1

            pos_initiale = ord(char) - ord('A')

            nouvelle_pos = (pos_initiale + decalage) % 26
            
            nouveau_char = chr(ord('A') + nouvelle_pos)
            resultat += nouveau_char
        else:
            resultat += char
            
    return resultat


print(decalage_cesar("AB", "BONJOUR"))

import random

def random_election(liste_noms):
    if len(liste_noms) < 4:
        raise ValueError("Il faut au moins 4 personnes dans la liste.")

    selection = random.sample(liste_noms, 4)
    
    resultat = {
        "délégués": [selection[0], selection[1]],
        "suppléants": [selection[2], selection[3]]
    }
    
    return resultat

etudiants = ["Alice", "Bob", "Charlie", "David", "Emma", "Fabien"]
print(random_election(etudiants))