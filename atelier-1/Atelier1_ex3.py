import math

# la forme ax²+bx+c =0 avec a,b,c réels et a≠0. 
# function discriminant(a,b,c) 

def discriminant(a,b,c):
    return  (float(b) ** 2) - (4 * float(a) * float(c)) 

# function racine_unique(a,b)
def racine_unique(a,b):
    (a,b) = (float(a),float(b))
    return -b / (2 * a)

# function racine_double(a,b,delta,num) 
def racine_double(a,b ,delta,num):
    (a,b) = (float(a),float(b))
    return (-b + math.sqrt(delta)) / (2 * a) if num == 1 else (-b - math.sqrt(delta)) / (2 * a)

# function str_equation(a,b,c) : 
def str_equation(a,b,c):
    (a,b,c) = (float(a),float(b),float(c))
    return ( str(a) if a > 1 else "" ) + "x²" + (" + " if b !=0 and b > 0  else ( " " if b < 0 else "" ))  + ( ( str(b) if (b != 0 and b > 1) or b < -1   else ("-" if b == -1 else "")) + ( "x" if b!= 0 else "")) + (" + " + str(c)  if c > 0 else ( " " + str(c) if c != 0 else "" ) )  + " = 0" 

# function solution_equation(a,b,c) :
def solution_equation(a,b,c) :
    dis = discriminant(a,b,c)
    return '''Solution de l'équation {equation}
            Pas de racine réelle" si l'équation n'a pas de solution réelle '''.format(equation=str_equation(a,b,c)) if dis < 0 else  ( '''Solution de l'équation {equation} Racine unique x= {racine} '''.format(equation=str_equation(a,b,c),racine = racine_unique(a,b)) if dis == 0 else '''Solution de l'équation {equation} Deux racines [ x1= {x1} , x2= {x2} ]'''.format(equation=str_equation(a,b,c),x1=racine_double(a,b,dis,1),x2=racine_double(a,b,dis,2)))

# function equation(a,b,c):
def equation(a,b,c) : 
    return  solution_equation(a,b,c) if discriminant(a,b,c) >= 0 else "aucune solution réelle" 

while True :
    a = input("entrer la valeur de a (a != 0) => ")
    b = input("entrer la valeur de b => ")
    c = input("entrer la valeur de c => ")
    if a == 0 :
        print("something weng wrong !!!")
    else :
        break

print(equation(a,b,c))