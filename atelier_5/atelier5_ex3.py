import numpy as np
from atelier5_ex2 import est_symetrique


def matriceAdjacence(S, A):
    return [[1 if (ligne, column) in A else 0 for column in range(len(S))] for ligne in range(len(S))]


def matriceAdjacencePond(S, A):
    result = [[0 for _ in range(len(S))] for _ in range(S[-1])]
    for item in A:
        (i, j, poids) = item
        result[i][j] = poids

    return result


print(matriceAdjacence([0, 1, 2, 3, 4], [(0, 1), (0, 2), (1, 2)]))

print(matriceAdjacencePond([0, 1, 2, 3, 4], [(0, 1, 3), (0, 2, 5), (1, 2, 5)]))


def lireMatriceFichier(nomfichier):

    file = open(nomfichier, "r")
    result, i = [], 0

    for ligne in file:
        result.append([])
        for sommet in ligne.strip().split(" "):
            result[i].append(int(sommet))

        i += 1
    return result


matrix = lireMatriceFichier("graphe0.txt")


def tousLesSommets(mat):
    return [sommet for sommet in range(len(mat))]


def listeArcs(mat):
    return [(ligne, column) for ligne in range(len(mat)) for column in range(len(mat)) if mat[ligne][column] != 0]


print(lireMatriceFichier("graphe0.txt"))
print(tousLesSommets(lireMatriceFichier("graphe0.txt")))
print(listeArcs(lireMatriceFichier("graphe0.txt")))


def matriceIncidence(mat):
    arcs, sommets = listeArcs(mat), tousLesSommets(mat)
    one_level_list_arcs = range(len(arcs))

    if est_symetrique(np.array(mat)):
        return np.array([[(1 if arcs[column][0] == ligne or arcs[column][1] == ligne else 0) for column in one_level_list_arcs] for ligne in range(len(sommets))])
    else:
        return np.array([[1 if arcs[column][0] == ligne else (-1 if arcs[column][1] == ligne else 0) for column in one_level_list_arcs] for ligne in range(len(sommets))])


print(matriceIncidence(lireMatriceFichier("graphe0.txt")))
