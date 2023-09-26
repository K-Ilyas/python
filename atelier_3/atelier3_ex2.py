


def  mots_Nlettres(lst_mot, n):
    return [mot for mot in lst_mot if len(mot) == n]


def commence_par(mot, prefixe):
    """
    """
    return mot[:len(prefixe)] == prefixe

def finit_par(mot,suffix):
    return mot[-len(suffix):] == suffix


def finissent_par(lst_mot, suffixe):
    return [mot for mot in lst_mot if finit_par(mot,suffixe)]


def commencent_par(lst_mot, prefixe):
    return [mot for mot in lst_mot if commence_par(mot,prefixe)]

def liste_mots (lst_mot, prefixe, suffixe, n) :
    return [mot for mot in lst_mot if commence_par(mot,prefixe) and finissent_par(mot,suffixe) and len(mot) == n]


def dictionnaire(fichier) :

    file = open(fichier,"+r")
    data = list()
    for line in file : 
        for word in list(filter(lambda x : x!= "", line.strip().split(" "))) :
            data.append(word)

    file.close()

    return data

# print(finit_par("ilyas","zas"))

# print(dictionnaire("fichier.txt"))