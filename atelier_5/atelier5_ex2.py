import numpy as np
import time ,random
from numpy.linalg import det


arr = np.array([1, 2, 3, 4, 5])

print(arr)

arr = np.array([6, 8, 7,9, 7])
x = np.searchsorted(arr, 7)
print("saerch sorted :",x)


arr = np.array([6, 8, 9, 45, 54, 7, 7])
x = np.searchsorted(arr, 7)
print(x)

start = time.perf_counter()


def my_searchsorted(lst, indice):
    if lst.size == 0:
        return -1
    else:
        index = 0
        for item in sorted(lst):
            if item == indice:
                return index
            index += 1
        return -1

print(my_searchsorted(arr, 7))


def my_where(lst, cond):
    if lst.size == 0:
        return -1
    else:
        print(lst)
        # test = lambda item : eval(cond.strip())
        index = 0
        listIndex = []
        for item in lst:
            if cond(item):
                listIndex.append(index)
            index += 1
        return listIndex


def my_where_cond(lst, cond):
    if lst.size == 0:
        return -1
    else:
        def test(item): return eval(cond.strip())
        return [lst[index] for index in range(len(lst)) if test(lst[index])]

print(my_where(arr, lambda item: item % 2 == 0))

print("with one step",my_where_cond(arr, "item > 2"))


def my_add(listA, listB):
    if listA.shape != listB.shape:
        return None
    else:
        result = []
        for row in range(listA.shape[0]):
            result.append([])
            for column in range(listA.shape[1]):
                result[row].append(listA[row][column]+listB[row][column])
        return result


A = np.array(([3, 1], [6, 4]))
B = np.array(([1, 8], [4, 2]))
print(my_add(A, B))


# deuxime partie

arr2 = np.arange(9).reshape(3, 3) + 1
print(arr2)

# print matrix


def print_matrix(lst):
    for row in range(lst.shape[0]):
        for column in range(lst.shape[1]):
            print(lst[row][column], end="")
        print("\n", end="")

def add_number(lst,number):
    for row in range(lst.shape[0]):
        for column in range(lst.shape[1]):
            lst[row][column] += number
        print("\n", end="")

def multiply_number(lst,number):
    for row in range(lst.shape[0]):
        for column in range(lst.shape[1]):
            lst[row][column] *= number
        print("\n", end="")

def second_ligne(lst):
    for column in range(lst.shape[1]):
            print(lst[1][column],end="")

    return lst[1]
    
def third_column(lst):
    for row in range(lst.shape[0]):
            print(lst[row][2],end="")
    
    return lst[:,2]

def matrix_2_2(lst):
    result = []
    for row in range(2):
        result.append([])
        for column in range(2):
            result[row].append(lst[row][column])
    return result


# print("third column",third_column(arr2))



def matrix_4_4_creation():
    return [ [ random.randint(0,10) for _ in range(4)] for _ in range(4) ]

def matrix_4_4_creation_identite():
    return [ [ 0 if row != column else 1  for column  in range(4) ] for row in range(4) ]

def matrix_trace(lst):
    return  sum([ (0 if row != column else lst[row][column]) for row in range(len(lst)) for column  in range(len(lst[row])) ])


def est_symetrique(lst):
   if  lst.shape[0] != lst.shape[1] :
       return False
   new_list = []
   length = range(len(lst))
   for row in length:
        new_list.append([])
        for new_column in length:
            new_list[row].append(lst[new_column][row])

   print(new_list)

   return  all([ True if all(item) else False for item in list(new_list == lst)])

print(matrix_trace(matrix_4_4_creation_identite()))
table = np.array([[1, 2, 3],[2, 9, 5],[3, 5, 6]])

print(est_symetrique(table))

def produit_diagonal_caree(lst):
    multiple = 1
    for item in  ([ (0 if row != column else lst[row][column]) for row in range(len(lst)) for column  in range(len(lst[row])) ]) :
            if item != 0 :
             multiple *= item
    return multiple

print(produit_diagonal_caree(table))



def transpose_matrix(lst):
    return  np.add(lst, lst.T) / 2

matriceA = np.array([[1,2,3],[3,34,5],[5,6,98]])
def inverse_matrix(lst):
    return np.dot(lst,np.linalg.inv(lst)) 


print(matrix_trace(matriceA))
print((transpose_matrix(matriceA)))
print(inverse_matrix(matriceA))
