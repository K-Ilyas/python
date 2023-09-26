import matplotlib.pyplot as plt
from Atelier2_ex1 import val_max

def histo(F):
    H = [0] * (val_max(F) +1) 
    for item in F:
        H[item] += 1 
    return H

print(histo([6,5,6,8,4,2,1,5]))


def est_injective(F) :
    return  len(list(filter(lambda x : x > 1,histo(F)))) == 0

def est_surjective(F):
    return  len(list(filter(lambda x : x < 1,histo(F)))) == 0

def est_bijective(F):
    return est_bijective(F) and est_injective(F) 

### display histograme :

def afficheHisto(F):

    print("TEST HISTOGRAME \n")
    print("F=",F,"\n")
    print("HISTOGRAME \n")

    histo_F = histo(F)
    length = val_max(histo_F)

    for i in range(length) :
     for index in range(len(histo_F)) : 
         if histo_F[index] >= 1 and length - i == histo_F[index] :
            print("   #",end='')
            histo_F[index] -= 1
         else :
            print("    ",end='')
     print("\n",end='')       
    
    print("\n|" + " --|" * len(histo_F),"\n",end='')

    for index in range(len(histo_F)) :
        print("  {0:2d}".format(index),end='')



def afficheHisto_maptolib(F):
    plt.subplots(figsize=(12,6))
    plt.title("histogram avec maptolib")
    plt.hist(F)
    plt.savefig("histogram")





### est_injective test  

# print(histo([6,5,6,7,4,2,1,5]))
# print(est_injective([6,5,6,7,4,2,1,5]))

# print(histo([3,0,6,7,4,2,1,5]))
# print(est_injective([3,0,6,7,4,2,1,5]))

# ### est_surjective test  

# print(histo([6,5,6,7,4,2,1,5]))
# print(est_surjective([6,5,6,7,4,2,1,5]))

# print(histo([3,0,6,7,4,2,1,5]))
# print(est_surjective([3,0,6,7,4,2,1,5]))

# ### est_surjective test  

# print(histo([6,5,6,7,4,2,1,5]))
# print(est_surjective([6,5,6,7,4,2,1,5]))

# print(histo([3,0,6,7,4,2,1,5]))
# print(est_surjective([3,0,6,7,4,2,1,5]))



# afficheHisto([1,5,5,5,9,11,11,15,15,15])
# afficheHisto_maptolib([1,5,5,5,9,11,11,15,15,15])


# afficheHisto([1,4,5,3,7,9,3,2,2,5,6])

print(histo([]))