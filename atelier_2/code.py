


def plus_proche_zero(L):
    plus_proche = L[0]
    for item in L:
        condition = (plus_proche if plus_proche > 0 else -1 * plus_proche )
        if  item > 0 and item < condition :
            plus_proche = item
        elif item < 0 and (item * -1 ) < condition:
            plus_proche = item
    
    return plus_proche


def plus_proche_zero_2(L):
    result = abs(L[0])
    for index in list(map(lambda x : x if x > 0 else x * -1,L)) :
        result = ( index if index < result else result)
    return result



print(plus_proche_zero([7,1,-10,13,8,4,-7.2,-12,-3.7,3.5,-1.7,2]))
print(plus_proche_zero_2([7,1,-10,13,8,4,-7.2,-12,-3.7,3.5,-1.7,2]))