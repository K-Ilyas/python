from atelier_4_ex2 import mix_list2
import time,random
import matplotlib.pyplot as plt
import numpy as np

def pref_mix(func1,func2,lst,num=10):
   result = ([],[])
   for elem in lst : 
    data1 ,data2= [],[]
    for index in range(num) : 
      lst_elem = list(range(elem))
      # first function
      start = time.perf_counter()
      func1(lst_elem)
      end = time.perf_counter() - start
      data1.append(end)

      start = time.perf_counter()
      func2(lst_elem)
      end = time.perf_counter() - start
      data2.append(end)
    result[0].append(sum(data1)/len(data1))
    result[1].append(sum(data2)/len(data2))

   
   
   return result
      
#    return ([func1(list(range(elem))) for elem in lst],[func2(list(range(elem))) for elem in lst])

list_test = [500,1000,2500,5000,7500]
result = pref_mix(mix_list2,random.shuffle, list_test ,100)
print(result)

#Ici on décrit les abscisses
#Entre 0 et 5 en 10 points
fig, ax = plt.subplots()
#Dessin des courbes, le premier paramètre 
#correspond aux point d'abscisse le
#deuxième correspond aux points d'ordonnées
#le troisième paramètre, optionnel permet de 
#choisir éventuellement la couleur et le marqueur
ax.plot(list_test,result[0], 'bo-',label='mix_list')
ax.plot(list_test,result[1], 'r*-', label='random.shuffle')



ax.set(xlabel='temps', ylabel='nombre d\'elements',
 title='temps d’exécution moyen pour mix_list et random.shuffle')
ax.legend(loc='upper center', shadow=True, fontsize='x-large')
#fig.savefig("test.png")
plt.show()





