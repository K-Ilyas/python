from atelier_4_ex1 import gen_list_random_int



def mix_list(lst_sorted) :
    list_sorted_length ,mix_length = len(lst_sorted) ,0
    mixList = list()
    
    while mix_length != list_sorted_length:
        random_ = gen_list_random_int(0,list_sorted_length)
        if random_ not in mixList :
            mix_length += 1
            mixList.append(random_)
    
    return [ lst_sorted[elem] for elem in mixList ]


def mix_list2(lst_sorted) :
    list_sorted_length = len(lst_sorted) 
    mixList = list()
    
    while list_sorted_length != 0:
        random_ = gen_list_random_int(0,len(lst_sorted))
        list_sorted_length -= 1
        mixList.append(lst_sorted[random_])
        del lst_sorted[random_]

    return mixList




print(mix_list([1,2,3,4,5,6,7,8,9,10]))