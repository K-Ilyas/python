def somme_recursive(liste1):
    if len(liste1) == 0:
        return 0
    else:
        return somme_recursive(liste1[:-1]) + liste1[-1]


print(somme_recursive([1, 2, 3, 4, 5]))


def factorielle_recursive(nombre):
    if nombre == 1:
        return 1
    else:
        return factorielle_recursive(nombre - 1) * nombre


print(factorielle_recursive(5))


def longeur(lst):
    if not lst:
        return 0
    else:
        return longeur(lst[:-1]) + 1


print(longeur([1, 2, 3, 4, 5, 6]))


def findMin(lst):
    try:
        if lst[1]:
            min = findMin(lst[:-1])
            return lst[-1] if lst[-1] < min else min
    except:
        return lst[-1]


def findMin2(lst):
    if lst[0] is lst[-1]:
        return lst[-1]
    else:
        min = findMin(lst[:-1])
        return lst[-1] if lst[-1] < min else min

print("Min : ", findMin2([4,1, 3, 4,4, -5, 6, -17, -2]))


def concat_list(lst):
    if not lst:
        return []
    else:
        result = concat_list(lst[:-1])
        
        return  result + (lst[-1] if isinstance(lst[-1], list) else [lst[-1]])

print(concat_list([[1, 2, 3], [1, 3, 4], 2, 98, 5,[1,5,4,78]]))


def separe(lst):
    if not lst:
        return ([], [])
    else:
        result = separe(lst[:-1])
        return (result[0] + [lst[-1]], result[1]) if lst[-1] % 2 != 0 else (result[0], result[1] + [lst[-1]])

print(separe([1, 23, 4, 5, 6, 9, 7, 4, 3]))

#  print(result[0])
#         if lst[-1] % 2 != 0:
#             result[0].append(lst[-1])
#         else:
#             result[1].append(lst[-1])