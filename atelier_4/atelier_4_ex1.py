import random

def gen_list_random_int(int_binf = 0,int_bsup = 10):
    return round(random.random() * int(int_bsup - int_binf -1) )

def gen_list_random_int_list(un_parametre_int=10,int_binf = 0,int_bsup = 10):
    return [round(random.random() * int(int_bsup - int_binf)) + int_binf for _ in range(un_parametre_int)]

# print(gen_list_random_int_list(5,0,6))