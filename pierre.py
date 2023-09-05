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
    n1 = questions(2)
    print("Bienvenu ",n1, " nous allons jouer ensemble \n")
    n2 = 'Machine' 

elif cpo == 'N':
    n1 = questions(2)
    print("Bienvenu ",n1, " nous allons jouer ensemble")
    n2 = questions(3)
    print("Bienvenu ",n2, " nous allons jouer ensemble \n")

np = 0
c = True
p2 = 0
s1 = 0
while c == True:
    np += 1 
    c1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux): ".format(nom=n1))
    # if c1 != 'pierre':
    #     if c1 != 'papier':
    #         if c1 != 'ciseaux':
    #             c1ok = False
    #             print("Je n'ai pas compris votre réponse")
    #             while c1ok == False :
    #                 print("Joueur ", n1)
    #                 c1 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
    #                 c1ok = True
    #                 if c1 != 'pierre': 
    #                     if c1 != 'papier':
    #                         if c1 != 'ciseaux':
    #                             c1ok = False
    
    # use a while lop instead of a il else statment
    while  c1 != 'pierre' and c1 != 'papier' and  c1 != 'ciseaux' :
        print("Je n'ai pas compris votre réponse")
        print("Joueur ", n1)
        c1 = questions(4)


    

    if n2 == 'Machine' and cpo == 'O': 
        #Ici il faudrait plutôt vérifier que cpo == 'O' autrement
        #il y a un problème si le joueur 2 s'appelle Machine !
        e2 = ['papier','pierre','ciseaux'][random.randint(0, 2)]
    else :
    # if n2 != 'Machine' and :
        print("Joueur", n2)
        e2 = input("faîtes votre choix parmi (pierre, papier, ciseaux): ")
        # if e2 != 'pierre':
        #     if e2 != 'papier':
        #         if e2 != 'ciseaux':
        #             j2bon = False
        #             print("Je n'ai pas compris votre réponse")
        #             while not j2bon :
        #                 print("Joueur ", n2)
        #                 e2 = input(" faîtes votre choix parmi (pierre, papier, ciseaux): ")
        #                 j2bon = True
        #                 if e2 != 'pierre': 
        #                     if e2 != 'papier':
        #                         if e2 != 'ciseaux':
        #                             j2bon = False

        # use a while lop instead of il else statment

        while  e2 != 'pierre' and e2 != 'papier' and  e2 != 'ciseaux' :
            print("Je n'ai pas compris votre réponse")
            print("Joueur ", n2)
            e2 = questions(4)


    #On affiche les choix de chacun
    print("Si on récapitule :",n1, c1, "et", n2, e2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat
    if c1 == 'papier' and e2 == 'papier' :
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0
        

    elif c1 == 'pierre' and e2 == 'papier' :
        w12 = n2
        s1 = s1 + 0
        p2 = p2 + 1

    elif c1 == 'pierre' and e2 == 'pierre' :
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0

    elif c1 == 'pierre' and e2 == 'ciseaux' :
        w12 = n1
        s1 = s1 + 1
        p2 = p2 + 0
    

    elif c1 == 'papier' and e2 == 'ciseaux' :
        w12 = n2
        s1 = s1 + 0
        p2 = p2 + 1

    elif c1 == 'papier' and e2 == 'pierre' :
        w12 = n1
        s1 = s1 + 1
        p2 = p2 + 0

    elif c1 == 'ciseaux' and e2 == 'pierre' :
        w12 = n2
        s1 = s1 + 0
        p2 = p2 + 1

    elif c1 == 'ciseaux' and e2 == 'ciseaux' :
        w12 = "aucun de vous, vous être ex æquo"
        s1 = s1 + 0
        p2 = p2 + 0

    elif c1 == 'ciseaux' and e2 == 'papier' :
        w12 = n1
        s1 = s1 + 1
        p2 = p2 + 0
        
    print("le gagnant est",w12)
    print("Les scores à l'issue de cette manche sont donc",n1, s1, "et", n2, p2, "\n")

    # if np ==1 or np ==2 or np==3 or np==4:
    #     c = True
    # if np ==5:
    #     c = False
        
    # if np ==1 or np ==2 or np==3 or np==4:
    #     #On propose de c ou de s'arrêter 
    #     go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(n1,n2))
    #     if go == 'O':
    #         c = True
    #     if go == 'N':
    #         c = False
    #     if go != 'O' and go != 'N':
    #         c = True
    #         print("Vous ne répondez pas à la question, on continue ")

    if np == 5 :
       c = False
    else :
       c = True
       #On propose de c ou de s'arrêter 
       go = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(n1,n2))
       if go == 'O':
            c = True
       elif go == 'N':
            c = False
       else :
            c = True
            print("Vous ne répondez pas à la question, on continue ")

  
        
# if c == False :
#     print("Merci d'avoir joué ! A bientôt")
else :
    print("Merci d'avoir joué ! A bientôt")