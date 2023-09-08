

def position_for(lst,elt):
    for index in range(len(lst)) :
        if lst[index] == elt :
            return index 
    return -1




def position_while(lst,elt):
    index = 0
    while index < len(lst):
        if lst[index] == elt :
            return index   
        index += 1      
    return -1


def nb_occurrences(lst,e):
    occurrence = 0
    for item in lst : 
        occurrence += 1 if item == e else 0
    return occurrence

def est_triee(lst):
    
    for index in range(len(lst)-1):
        if lst[index+1] < lst[index]:
          return False
    return True

def est_triee_while(lst):
    index = 0
    length = len(lst) - 1
    while index < length:
        if lst[index+1] < lst[index]:
          return False
        index += 1
    return True

def position_tri(lst,e) :
    x = 0 
    y = len(lst) -1 

    while x <= y :
        v = int((x + y) /2)
        if lst[v] == e :
          return v
        if lst[v] < e :
           x += 1 
        else : 
           y -= 1
    return -1
          


def a_repetitions(lst):
    
    for index in range(len(lst)):
        if lst[index] in lst[0:index]+lst[index+1:] :
            return True
    return False

print(a_repetitions([1,3,4,5,6]))


