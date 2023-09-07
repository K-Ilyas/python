# Pour savoir si un nombre x est divisible par 4 (par ex), il suffit de tester que le
# reste de sa division par 4 est égal à 0. L'opérateur modulo (noté % en python) fait cette
# opération. Ainsi si x%4==0, cela signifiera que x est divisible par 4.


# function definition :

def annee_bissextile(annee):
    return annee % 4 == 0 and annee % 100 != 0 and annee % 400 !=0

