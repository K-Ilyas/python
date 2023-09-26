from atelier_4_ex1 import gen_list_random_int
import time


def choose_element_list(list_in_which_to_choose):
    return list_in_which_to_choose[gen_list_random_int(0,len(list_in_which_to_choose))]


start =  time.perf_counter()




lst_sorted = [ i for i in range(1,11)]
# Test de votre code
print('Liste triée de départ',lst_sorted)
e1 = choose_element_list(lst_sorted)
print('A la première exécution',e1,'a été sélectionné')
e2 = choose_element_list(lst_sorted)
print('A la deuxième exécution',e2,'a été sélectionné')
assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"

print(time.perf_counter() - start)
