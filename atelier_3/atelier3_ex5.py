
import re


def ouvrante(car):
    return car in ['(', '[', '{']

# print(ouvrante("("))


def fermante(car):
    return car in [')', ']', '}']


def renverse(car):
    dict = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    return dict[car] if fermante(car) else (car if ouvrante(car) or re.search("^((-){0,1}([\d]+|[\d]+\.[\d]+)|[\+\-\/\*\+\%]|\s)$", car) else None)


def operateur(car):
    return car in ["+", "-", "*"]


def nombre(car):
    return True if re.search("^(-){0,1}([\d]+|[\d]+\.[\d]+)$", car) else False


def caractere_valide(car):
    return True if ouvrante(car) or fermante(car) or operateur(car) or nombre(car) or re.search("^\s$", car) else False


# print(nombre("-12"))


def verif_parenthese(expression):
    verify_caracteres = all([True if (ouvrante(car) or fermante(car) or operateur(
        car) or nombre(car) or re.search("^\s$", car)) else False for car in expression])
    if verify_caracteres:
        pile = [parenthese for parenthese in expression if ouvrante(
            parenthese) or fermante(parenthese)]
        print(pile)
        if len(pile) % 2 == 0:
            return all([True if pile[index] == renverse(
                pile[-1 - index]) else False for index in range(0, int((len(pile)/2)))])
        else:
            return False
    else:
        return False


print(verif_parenthese("(3+2) * 6-1"))
print(verif_parenthese("((3+2)*6-1"))
print(verif_parenthese("(5+7]*12"))
print(verif_parenthese("[(5+7])*12"))
