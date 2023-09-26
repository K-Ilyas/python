
from atelier3_ex2 import mots_Nlettres
from atelier3_ex3 import build_list

def mot_correspond(mot, motif):
    return False if mot == "" or motif == "" or len(mot) != len(motif) else  ( True if all([ (True if motif[index] ==  "." or motif[index] == mot[index] else False ) for index in range(len(mot)) ]) else False)  
   


# print(mot_correspond("tarte", "t..t."))
# print(mot_correspond("cheval", "c..v..l"))
# print(mot_correspond("cheval", "c..v.l"))


def presente(lettre, mot) : 
    
    return mot.index(lettre) if len(mot) != 0 and lettre in mot  else -1

# print(presente("",""))

def mot_possible(mot, lettres) :
    for letter in mot : 
        if presente(letter,lettres) != -1 :
            lettres = lettres.replace(letter,"",1)
        else :
            return False
    return True


# print(mot_possible("lapin", "abilnpq"))
# print(mot_possible("cheval", "abilnpq"))
# print(mot_possible ("chapeau", "abcehpuv"))
# print(mot_possible ("chapeau", "abcehpuva"))




def mot_optimaux(dico,letters):
    return [ mot for mot in mots_Nlettres(dico,len(letters)) if mot_possible(mot,letters.lower())]




print(mot_optimaux(build_list("capitales.txt"),"mpsCa"))