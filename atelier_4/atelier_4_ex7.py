import sys
sys.path.append('../')

from atelier_2.Atelier2_ex2 import est_triee
from atelier_4_ex2 import mix_list


# Tri	stupide
def stupid_sort(lst):
    lst_copy = lst.copy()
    while not est_triee(lst_copy):
        lst_copy = mix_list(lst_copy)
    return lst_copy


print(stupid_sort([-2,34,-10,1,4,66,4,109]))


# le tri par	insertion
def insertion_sort(lst):
    lst_copty = lst.copy()
    for i in range(1,len(lst_copty)):
        x = lst_copty[i]   
        j = i 
        while j > 0 and lst_copty[j-1] > x :
            lst_copty[j] = lst_copty[j-1]
            j -= 1
        lst_copty[j] = x
    return lst_copty

my_lst_to_sort = [170, 45, 75, 90, 2, 24, 802, 66] 
print(insertion_sort(my_lst_to_sort))



# le tri	par	sélection


def tri_selection(lst,  n=0):
    lst_copy = lst.copy()
    for i in range(0,len(lst_copy)-1):
        min = i
        for j in range(i+1,len(lst_copy)):
            if lst_copy[j] < lst_copy[min]:
                min = j
        if min != i :
            lst_copy[i],lst_copy[min] = lst_copy[min],lst_copy[i]
    
    return lst_copy

print(tri_selection(my_lst_to_sort))


# 	le	tri	à	bulle

def tri_à_bulles_optimisé(lst):
    lst_copy = lst.copy()
    print( list(range(len(lst_copy),0,-1)))
    for index in range(len(lst_copy),0,-1):
      lst_verified = True 
      for index2 in range(0,index-1):
        if lst_copy[index2+1 ] < lst_copy[index2]:
            lst_copy[index2+1 ] , lst_copy[index2] = lst_copy[index2], lst_copy[index2+1 ]
            lst_verified = False
      if lst_verified :
        break
      
    return lst_copy


print(tri_à_bulles_optimisé(my_lst_to_sort))




# tri par fussion 

# def triFusion(lst):
#     n = len(lst)
#     if n <= 1:
#         return lst 
#     else :
#         center = n/2 if n ()
#         return fusion(triFusion(lst[:round(n/2)]),triFusion(lst[int(n/2):]))
    
# def fusion(A,B):
#     print( A[1] ,B[1])
#     if len(A) == 0 :
#         return B
#     elif len(B) == 0 :
#         return A
#     elif A[1] <= B[1] :
#         return A[1] + fusion(A[2:],B)
#     else :
#         return  B[1] + fusion(B[2:],A)


# print(triFusion(my_lst_to_sort))
