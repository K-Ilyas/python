# boucle 

list_int = list((1,99,1,1,1,-2,3))

def somme_range(list_in):
 sum = 0
 for index in range(len(list_int)):
   sum += list_in[index]
 return sum 

def somme_in(list_in):
  sum = 0
  for item in list_int : 
   sum +=  item
  return sum 
    
def somme_while(list_in):
 
 i,somme=len(list_int) - 1 ,0
 while i >= 0:
    somme += list_in[i]
    i -= 1
 return somme

def somme_listcomp(list_in):
    return sum(list_in)


def moyenne(l):
   return somme_while(l) / len(l) if len(l) != 0 else 0
     

def nb_sup_range (L,e) :
    nb_sup = 0
    for index in range(len(L)):
        nb_sup +=  (1 if  L[index] > e else 0)
    return nb_sup

def nb_sup_for (L,e) :
    nb_sup = 0
    for index in range(len(L)):
        nb_sup += (1 if  L[index] > e else 0)
    return nb_sup

def moy_sup(L,e) : 
    somme = 0
    for item in L:
        somme += (item if item > e else 0)
    return somme / nb_sup_for(L,e)


def val_max(L):
    max_ = 0 
    for item in L :
        (max_ := item  if item > max_ else max_)
    return max_

def ind_max(L):
    index_max = 0
    for index in range(len(L)):
        if L[index] == val_max(L) :
         return index
        else :
            continue



print(val_max(list_int))

