import random

def questions(code) :
    match code :
        case 1 :
            return input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ? " )
        case 2 :
            return input("Quel est votre nom ? ")
        case 3 :
           return  input("Quel est le nom du deuxième joueur ?")
        case 4 :
           return input("faîtes votre choix parmi (pierre, papier, ciseaux): ")

cpo = questions(1)
while cpo != 'O' and cpo != 'N':
    # if cpo != 'N' : // 
    print("Je n'ai pas compris votre réponse")
    cpo = questions(1)

if cpo == 'O':
    joueur1 = questions(2)
    print("Bienvenu ",joueur1, " nous allons jouer ensemble \n")
    joueur2 = 'Machine' 

elif cpo == 'N':
    joueur1 = questions(2)
    print("Bienvenu ",joueur1, " nous allons jouer ensemble")
    joueur2 = questions(3)
    print("Bienvenu ",joueur2, " nous allons jouer ensemble \n")

np = 0
c = True
joueur2_result = 0
joueur1_result = 0
while c == True:
    np += 1 
    joueur1_choice = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, puit): ".format(nom=joueur1))
   
    # use a while lop instead of a il else statment
    while  joueur1_choice != 'pierre' and joueur1_choice != 'papier' and  joueur1_choice != 'ciseaux' and joueur1_choice !='puit' :
        print("Je n'ai pas compris votre réponse")
        print("Joueur ", joueur1)
        joueur1_choice = questions(4)
    if joueur2 == 'Machine' and cpo == 'O': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        joueur2_choice = ['papier','pierre','ciseaux','puit'][random.randint(0, 2)]
    else :
    # if joueur2 != 'Machine' and :
        print("Joueur", joueur2)
        joueur2_choice = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
       

        # use a while lop instead of il else statment

        while  joueur2_choice != 'pierre' and joueur2_choice != 'papier' and  joueur2_choice != 'ciseaux' and joueur2_choice !='puit':
            print("Je n'ai pas compris votre réponse")
            print("Joueur ", joueur2)
            joueur2_choice = questions(4)


    #On affiche les choix de chacun
    print("Si on récapitule :",joueur1, joueur1_choice, "et", joueur2, joueur2_choice,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if joueur1_choice == joueur2_choice :
        winner = "aucun de vous, vous être ex æquo"
        joueur1_result = joueur1_result + 0
        joueur2_result = joueur2_result + 0
        
    elif (joueur1_choice == 'pierre' and joueur2_choice == 'papier') or (joueur1_choice == 'papier' and joueur2_choice == 'ciseaux') or (joueur1_choice == 'ciseaux' and joueur2_choice == 'pierre') or (joueur1_choice == 'puit' and joueur2_choice == 'papier' ) or (joueur2_choice == 'puit' and joueur1_choice != 'papier' ) :
        winner = joueur2
        joueur1_result = joueur1_result + 0
        joueur2_result = joueur2_result + 1

    elif (joueur1_choice == 'pierre' and joueur2_choice == 'ciseaux' ) or  ( joueur1_choice == 'papier' and joueur2_choice == 'pierre') or (joueur1_choice == 'ciseaux' and joueur2_choice == 'papier' ) or (joueur1_choice == 'puit' and joueur2_choice != 'papier') or (joueur2_choice == 'puit' and joueur1_choice == 'papier'):
        winner = joueur1
        joueur1_result = joueur1_result + 1
        joueur2_result = joueur2_result + 0

    print("le gagnant est",winner)
    print("Les scores à l'issue de cette manche sont donc",joueur1, joueur1_result, "et", joueur2, joueur2_result, "\n")

    if np == 5 :
       c = False
    else :
       c = True
       #On propose de c ou de s'arrêter 
       go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(joueur1,joueur2))
       if go == 'O':
            c = True
       elif go == 'N':
            c = False
       else :
            c = True
            print("Vous ne répondez pas à la question, on continue ") 
else :
    print("Merci d'avoir joué ! A bientôt")