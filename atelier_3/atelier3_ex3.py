
import random
import re
import math


def places_lettre(ch: str, mot: str):
    return [index for index in range(len(mot)) if mot[index] == ch]


def outputStr(mot: str, lpos: list):
    return "".join([("_" if index not in lpos else str(mot[index])) for index in range(len(mot))])

# print(outputStr('bonjour',[]))
# print(outputStr('bonjour',[0]))
# print(outputStr('bonjour',[0,1,4]))
# print(outputStr('bon',[0,1,2]))
# print(outputStr('maman',[1,3]))


def build_list(fileName: str):
   # lire un fichier
    file = open(fileName or "capitales.txt", "r")
    content = file.readlines()
    words = []
    for line in content:
        for word in list(filter(lambda x: x not in ["", "\n"], line.split("\n|\t| "))):
            words.append(word.strip().lower())
    file.close()
    return words


def build_dict(fileName: str):
   # lire un fichier
    file = open(fileName or "capitales.txt", "r")
    content = file.readlines()
    words = {}
    for line in content:
        for word in list(map(lambda x: x.strip(), filter(lambda x: x not in ["", "\n"], line.split("\n|\t| ")))):
            length = len(word)
            if words.get(length):
                words[length].append(word.lower())
            else:
                words[length] = [word.lower()]
    file.close()
    return words
# print(build_dict(""))


def select_word(sorted_words: dict, word_len: int):
    length = len(sorted_words.get(word_len, ''))
    return sorted_words[word_len][random.randint(0, length-1)] if word_len in sorted_words.keys() else None


# print(select_word(build_dict(""),21))


def runGame_v1():
    lst = ["paris", "londres", "madrid", "berlin", "new-york"]
    iRand = random.randint(0, len(lst))
    word, place_letters = build_list("capitales.txt")[iRand - 1], []
    word_shadow, attempt = "_" * len(word), len(word) * 2
    print("Hello your word is => ", word_shadow, word)
    while word_shadow != word and attempt != 0:
        letter = str.strip(input("Enter your letter =>")).lower()
        print(letter and letter[0] in word)
        if letter and letter[0] in word:
            place_letters.extend(places_lettre(letter[0], word))
            place_letters = sorted(place_letters)
            word_shadow = outputStr(word, place_letters)
        print("L'etat actuel est => ", word_shadow)
        attempt -= 1
        if attempt >= 1:
            print("il vous reste ", attempt, " coups")
        if word_shadow == word:
            print("Bravo vous averz trouver le mot ", word)
            break
    else:
        print("|---] ")
        print("| O ")
        print("| T ")
        print("|/ \ ")
        print("|______")


def runGame_v2():
    lst = ["paris", "londres", "madrid", "berlin", "new-york"]
    difficulty = 0
    while difficulty not in [1, 2, 3]:
        print("select a level of difficulty => ")
        print('''
        • niveau ‘easy’ taille du mot < 7
        • niveau ‘normal’ 6 < taille du mot < 9
        • niveau ‘hard’ taille du mot > 8 ''')
        difficulty = str.strip(input("Enter your letter =>"))
        difficulty = int(difficulty[0]) if re.search("^\d", difficulty) else 0
    levels = [(1, 7), (6, 9), (8, math.inf)]
    level_difficulty = levels[difficulty-1]
    words = build_dict("capitales.txt")
    table_of_items = []
    for item in build_dict("capitales.txt").keys():
        if item > level_difficulty[0] and item < level_difficulty[1]:
            table_of_items.append(item)
    print(table_of_items[random.randint(0, len(table_of_items)-1)])
    word, place_letters = select_word(
        words, table_of_items[random.randint(0, len(table_of_items)-1)]), []
    word_shadow, attempt = "_" * len(word), len(word) * 2
    print("Hello your word is => ", word_shadow, word)
    while word_shadow != word and attempt != 0:
        letter = str.strip(input("Enter your letter =>")).lower()
        print(letter and letter[0] in word)
        if letter and letter[0] in word:
            print("wow*******")
            place_letters.extend(places_lettre(letter[0], word))
            place_letters = sorted(place_letters)
            word_shadow = outputStr(word, place_letters)
        print("L'etat actuel est => ", word_shadow)
        attempt -= 1
        if attempt >= 1:
            print("il vous reste ", attempt, " coups")
        if word_shadow == word:
            print("Bravo vous averz trouver le mot ", word)
            break
    else:
        print("|---] ")
        print("| O ")
        print("| T ")
        print("|/ \ ")
        print("|______")


# runGame_v2()


# x = requests.get('https://w3schools.com/python/demopage.htm')
