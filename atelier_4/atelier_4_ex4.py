from atelier_4_ex1 import gen_list_random_int

import matplotlib.pyplot as plt
import numpy as np
import time ,random



def extract_elements_list(list_in_which_to_choose,int_nbr_of_element_to_extract=10):
     list_in_which_to_choose_length,mix_length  = len(list_in_which_to_choose),0
     mixList = list()
     while mix_length < int_nbr_of_element_to_extract :
        random_ = gen_list_random_int(0,list_in_which_to_choose_length)
        if random_ not in mixList :
            mixList.append(random_)
            mix_length += 1
        else :
            continue

     return [ list_in_which_to_choose[elem] for elem in mixList ]


# Test de votre code

# def extract_elements_list2(list_in_which_to_choose,int_nbr_of_element_to_extract=10):
#      list_in_which_to_choose_length,mix_length  = len(list_in_which_to_choose),0
#      mixList = list()
#      while mix_length < int_nbr_of_element_to_extract :
#         random_ = gen_list_random_int(0,list_in_which_to_choose_length)
#         mixList.append(random_)
#         mix_length += 1
   

#      return [ list_in_which_to_choose[elem] for elem in mixList ]



# print(extract_elements_list( [ i for i in range(1,11)],4))




def pref_mix(func1,func2,lst,num=100):
   
   result = ([],[])

   for elem in lst : 
    data1 ,data2= [],[]
    nb_elements = int(elem / 2)
    for index in range(num) : 
      lst_elem = list(range(elem))
      # first function
      start = time.perf_counter()
      func1(lst_elem,nb_elements)
      end = time.perf_counter() - start
      data1.append(end)

      start = time.perf_counter()
      func2(lst_elem,nb_elements)
      end = time.perf_counter() - start
      data2.append(end)
    result[0].append(sum(data1)/len(data1))
    result[1].append(sum(data2)/len(data2))
   return result
      

list_test = [500,1000,2500,5000,7500]

result = pref_mix(extract_elements_list,random.sample, list_test ,100)

print(result)

#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre 
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de 
#choisir éventuellement la couleur et le marqueur

ax.plot(list_test,result[0], 'bo-',label='extract_elements_list')
ax.plot(list_test,result[1], 'r*-',label='random.sample')

ax.set(xlabel='temps', ylabel='nombre d\'elements',
 title='temps d’exécution moyen pour extract_elements_list et random.sample')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()


