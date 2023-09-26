import random,time
import matplotlib.pyplot as plt
import numpy as np

def sort_list(lst):
    new_lst = lst.copy()
    for index in range(len(new_lst)):
      for index2 in range(index,len(new_lst)) : 
        if new_lst[index] > new_lst[index2] :
            new_lst[index] ,new_lst[index2]  = new_lst[index2] ,new_lst[index]

    return new_lst


def pref_mix(func1,func2,lst,num=10):
   
   result = ([],[])
   data1 ,data2= [],[]

   for elem in lst : 
      for i in range(num) :
      # first function
       start = time.perf_counter()
       func1(elem)
       end = time.perf_counter() - start
       data1.append(end)

       start = time.perf_counter()
       func2(elem)
       end = time.perf_counter() - start
       data2.append(end)
      result[0].append(sum(data1)/len(data1))
      result[1].append(sum(data2)/len(data2))
   return result
      


conf1 = list(range(100))
random.shuffle(conf1)
conf2 = list(range(500))
conf3 = list(range(9999,-1,-1))

# print(conf1 ,"\n",conf2 ,"\n",conf3)


result = pref_mix(sort_list,sorted,[conf1,conf2,conf3],10)

print(result)



#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre 
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de 
#choisir éventuellement la couleur et le marqueur
y = [100,500,1000]
ax.plot(result[0], y, 'bo-',label='sort_list')
ax.plot(result[1],y, 'r*-', label='sorted')

ax.set(xlabel='temps', ylabel='nombre d\'elements',
 title='temps d’exécution moyen pour sort_list et sorted')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()


