# message_inc 


DICT_IMC = {
    16.5 : 'dénutrition ou famine',
    (16.5,18.5) :'maigreur',
    (18.5, 25) :'corpulence normale',
    (25 , 30): 'surpoids',
    (30 , 35): 'obésité modérée',
    (35 , 40) :'obésité sévère',
    40 : 'obésité morbide',
}



# function definition :

def message_inc(num):
    keys = list(DICT_IMC.keys())
    print(keys)
    return [Interpretation for (imc,Interpretation) in list(DICT_IMC.items()) if ( imc == keys[0] and num < imc) or (type(imc) == tuple and num >= imc[0] and num < imc[1] ) or (imc == keys[-1] and num >= imc)][0]




print(message_inc(16.5))