
def separer(L) :
    positif,negatif,null = list(),list(),list()

    for item in L :
        if item > 0 :
         positif += [item]
        elif item < 0 :
         negatif += [item]
        else :
         null += [0]
    
    return negatif + null + positif





print(separer([1,-1,0,2,0,4,0,-10]))