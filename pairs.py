

def ListPairs(lst):
    if len(lst) == 0:
        return []
    else :
        newList = ListPairs(lst[:-1])
        if  lst[-1] % 2 == 0 :
           newList.append(lst[-1])
        return newList


print(ListPairs([1,2,3,4,5,6,7,8]))