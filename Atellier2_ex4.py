from Atelier2_ex1 import val_max

def histo(F):
    H = [0] * (val_max(F) +1) 
    length = len(H)
    for item in list(filter(lambda x : x <= length -1 ,F)) :
        H[item] += 1 
    return H



print(histo([6,5,6,8,4,2,1,5]))


def est_injective(F) :
    return False if len(list(filter(lambda x : x > 1,histo(F)))) != 0 else True

def est_surjective(F):
    return False if len(list(filter(lambda x : x < 1,histo(F)))) != 0 else True


print(histo([6,5,6,7,4,2,1,5]))
print(est_injective([6,5,6,7,4,2,1,5]))

print(histo([3,0,6,7,4,2,1,5]))
print(est_injective([3,0,6,7,4,2,1,5]))

print(histo([6,5,6,7,4,2,1,5]))
print(est_surjective([6,5,6,7,4,2,1,5]))


print(histo([3,0,6,7,4,2,1,5]))
print(est_surjective([3,0,6,7,4,2,1,5]))

