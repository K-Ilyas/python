import re

# Simulation d’affranchissement lettre

# POIDS CONSTANT
POIDS_MINIMAL = 20 

# function for question 

def user_questions(num):
    match num:
     case 1 :
        return str.strip(input("faîtes votre choix parmi (LETTRE VERTE -> LV,LETTRE PRIORITAIRE => LP,ECOPLI => LE ,COLISSIMO ECO OUTRE-MER -> LOM ,CÉCOGRAMME => LC) => "))
     case 2 :
        return str.strip(input("le poids de votre lettre avec l'unite de mesure soit le gramme (g) et le kilogramme (kg)  => "))
     case 3:
        return str.strip(input('''Choisissez la destination de la lettre :
                    OM1 : Guyane, Guadeloupe, Martinique, La Réunion, St Pierre et Miquelon, St Barthélémy, St-Martin et Mayotte
                    OM2 : Nouvelle-Calédonie, Polynésie française, Wallis-et-Futuna,T.A.A.F.
                    => '''))

def messages(num,poids = None):
    match num:
      case 1 :
        print("le type de la lettre doit etre soit (LETTRE VERTE -> LV,LETTRE PRIORITAIRE => LP,ECOPLI => LE ,COLISSIMO ECO OUTRE-MER -> LOM ,CÉCOGRAMME => LC)")
      case 2 :
        print("le poids de votre lettre avec l'unite de mesure soit le gramme (g) et le kilogramme (kg) et doit commencer avec un nomber valid")
      case 3 :
        print("le poids de la lettre doit être entre 20g et {poids}g inclusive".format(poids=poids))
      case 4 :
        print("la destination doit etre soit OMI1 ou OMI2")


# POIDS : TARIFS 
POIDS_TARIFS = {
    'LV' :{
        20  :1.16,
        100 : 2.32,
        250 : 4.00,
        500 : 6.00,
        1000   : 7.50 ,
        3000   : 10.50,
        'OMI1' : 0.05,
        'OMI2' : 0.11
    },
    'LP':{
        20  :1.43,
        100 :2.86,
        250 : 5.26,
        500 : 7.89,
        3000   : 11.44,
        'OMI1' : 0.05,
        'OMI2' : 0.11
    },
    'LE' :{
        20  : 1.14,
        100 : 2.28,
        250 : 3.92,
        'OMI1' : 0.02,
        'OMI2' : 0.05
    },
    'LOM':{
        0.5 : 8.35,
        1000   :11.20,
        2000   : 14.10,
        5000   : 23.65,
        10000  : 37.50,
        15000  : 75.85,
        30000  : 87.40
    },
    'LC':0
}

while True :

  type_lettre = user_questions(1).upper()
  poids_search = re.search('(\d+\.?\d*)(g|kg)',user_questions(2),flags=re.IGNORECASE)
  poids_split = None if poids_search is None else poids_search.group(1,2)
  destination_lettre = user_questions(3).upper()
  
  # get the type of letter
  type_lettre_dict = POIDS_TARIFS.get(type_lettre)

  if type_lettre_dict is None :
    messages(1)    
  elif poids_search is None:
    messages(2)    
  elif poids_search is not None and (float(( float(poids_split[0])  if poids_split[1].lower() == 'g' else float(poids_split[0])*1000)) > int(max([ x for x in list(type_lettre_dict.keys()) if x != 'OMI1' and x != 'OMI2'])) or float(poids_split[0]) < POIDS_MINIMAL ):
    messages(3,int(max([ x for x in list(type_lettre_dict.keys()) if x != 'OMI1' and x != 'OMI2'])))    
  elif destination_lettre != 'OMI1' and destination_lettre != 'OMI2' :
    messages(4)
  else :
    break

poids = float(poids_split[0])
if poids_split[1].lower() == 'kg' :
    poids = poids * 1000

# get the type of letter
type_lettre_dict = POIDS_TARIFS.get(type_lettre)

# get the weight of the letter
poids_lettre_dict_value = list(filter(lambda x: x >= poids, [ x for x in list(type_lettre_dict.keys()) if x != 'OMI1' and x != 'OMI2']))[0]

# simulaion de resultat

verify_type = type_lettre not in ['LOM','LC']

simulation_affranchissement = type_lettre_dict[poids_lettre_dict_value] + ( type_lettre_dict[destination_lettre] * round(poids/10) if verify_type else 0 ) + (0.5 if verify_type and input("voulez-vous suiver votre commande ? O/N => ").upper() =='O' else 0)


print("{:.2f} €".format(simulation_affranchissement))




