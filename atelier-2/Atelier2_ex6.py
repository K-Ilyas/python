def present(L, e):
    for item in L:
        if e == item:
            return True
    return False


# # Question 5 : 


def pos(L,e):
    return [index for index in range(len(L)) if L[index] == e]



print(pos([3,4,5,7,2,7],7))