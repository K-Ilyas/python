import datetime
from Atelier1_ex2 import annee_bissextile

print(user_questions(1))

# funtion date_est_valide(jour,mois,annee)  
MONTH_DAYS = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}

def date_est_valide(jour,mois,annee):
    return False if  (isinstance(jour, int) and jour >=1 and jour <=  MONTH_DAYS[mois]) and (isinstance(mois, int) and mois >= 1 and mois <= 12 ) and (isinstance(anee, int)and len(str(annee)) == 4 )  else True

def saisie_date_naissance():
    while True :
     (jour,mois,annee)= (input("jour => "),input("mois => "),input("annee => "))
     verify_date =date_est_valide(jour,mois,annee)
     if verify_date :
        break

    return datetime.datetime(annee,mois,jour)
