
def separer(L):
    result = list()
    for item in L:
        if item > 0:
            result.append(item)
        elif item < 0:
            result.insert(0,item)
        else:
            result.insert(int(len(result)/2),0)
    return result

def separer_recursive(L):
    if len(L) == 0:
        return []
    else:
        result = separer_recursive(L[:-1])
        result.insert(int(len(L)/2), 0) if L[-1] == 0 else result.append(
            L[-1]) if L[-1] >= 0 else result.insert(0, L[-1])
        return result


print(separer([1, -1, 0, 2, 0, 4, 0, -10]))
