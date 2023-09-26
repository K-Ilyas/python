import re 
def full_name(str):
    str = str.strip()
    if str != "":
     result = str.split(" ")
     result[0] = result[0].upper()
     for i in range(1,len(result)):
       result[i] = result[i].lower().capitalize()
     return  (" ").join(result)
    else :
        return ""


# print(full_name("kritet AhmeD AmIne"))


def is_mail(str):
 if str.strip() != "" :
    corp_email = "^(?>([\w\-\_]+(\.){0,1}[\w\-\_]*){1,}[\w\-\_]+(?<!\.))"
    domaine_email = "(?<=\@)(?>[\w\-]+)"
    point = "(?<=[\w])(?>(\.)[\w]+){1,}$"
    result = re.search(corp_email + "(\@)" + domaine_email +point ,str.strip()) 
    if result : 
        return (1,0)
    else :
        if not re.search(corp_email,str) :
            return (0,1)
        elif not re.search("(\@)",str) :
            return (0,2)
        elif not re.search(domaine_email,str) :
            return (0,3)
        elif not re.search(point,str) :
            return (0,4)
        else :
            return "Something went wrong"
 else :
        return "The string in empty"


# print(is_mail("bisgambiglia_paulOuniv-corse.fr"))

str_variable2test = "bisgambiglia_paul@@univ-corse.fr"
print(is_mail(str_variable2test))  


# str_variable2test = "bisgambiglia_paul@univ-corse.fr"
# print(is_mail(str_variable2test))  # doit renvoyer (1,0)
# str_variable2test = "bisgambiglia_paulOuniv-corse.fr"
# print(is_mail(str_variable2test))  # doit renvoyer (0,2)
# str_variable2test = "bisgambiglia_paul@univ-corsePOINTfr"
# print(is_mail(str_variable2test))  # doit renvoyer (0,4)
# str_variable2test = "@univ-corse.fr"
# print(is_mail(str_variable2test))  # doit renvoyer (0,1)

# print(is_mail("20231699@webmail.universita.corsica"))  # doit renvoyer (0,1)
