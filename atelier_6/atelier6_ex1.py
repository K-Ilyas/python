def listeMultiples(binf,bsup,nb):
    return [ x * nb for x in range(1,10) if  binf <= x * nb <= bsup ]



print(listeMultiples(10,50,10))