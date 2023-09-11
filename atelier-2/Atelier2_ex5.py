# # vitrine
import time


# def vitrine(nbEmplacements: int, lObjets: list):
#     vitrine,turn  = [[],[]],  0
#     for item in lObjets:
#             vitrine[turn].insert(0, item) if len(vitrine[turn]) < nbEmplacements and item not in vitrine[turn]  else None
#             turn = (0 if turn == 1 else 1)
#     return vitrine



def vitrine_recursive(nbEmplacements: int, lObjets: list,turn:int = 0):
    if len(lObjets) == 0:
        return [[], []]
    else:

        result = vitrine_recursive(nbEmplacements, lObjets[:-1],1 if turn == 0 else 0)
        if len(result[turn]) < nbEmplacements and lObjets[-1]  not in result[turn] : 
            result[turn].append(lObjets[-1]) 
        else :
            change = (0 if turn == 1 else 1)
            result[change].append(lObjets[-1]) if len(result[change]) < nbEmplacements and lObjets[-1]  not in result[change]  else None
             
        return result


# start = time.time()

# print(vitrine(4, [1, 2, 2, 3, 4, 5, 5]))

# print(time.time() - start)



def vitrine2(nbEmplacements: int, lObjets: list):
    vitrine,turn  = [[],[]],  0
    test = lambda vitrine,item : len(vitrine) < nbEmplacements and item not in vitrine
    for item in lObjets:
            if test(vitrine[turn],item) : 
                vitrine[turn].insert(0, item) 
            else :
                change = (0 if turn == 1 else 1)
                vitrine[change].insert(0, item) if test(vitrine[change],item)  else None
            turn = (0 if turn == 1 else 1)
    return vitrine

print(vitrine2(6, [1, 1, 1, 3, 4, 5, 5,8,1,8,9]))
print(vitrine_recursive(6, [1, 1, 1, 3, 4, 5, 5,8,1,8,9]))
