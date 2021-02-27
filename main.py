slovnik = {"Bob": "123", "ann": "pas123", "mike": "password123", "liz": "pas123"}

name = input("Enter your username:")
password = input("Enter your password:")

if slovnik.get(name) == password:
    print("Thank you for registration.")

elif slovnik.get(name) != password:
    print("Wrong username or password, please try again.")
    quit()

if name in slovnik:
    print("Welcome to the app:", name)
    print("We have three texts, choose one for analysis")
    print('=' * 40)

    TEXTS = ('''
    Situated about 10 miles west of Kemmerer, 
    Fossil Butte is a ruggedly impressive 
    topographic feature that rises sharply 
    some 1000 feet above Twin Creek Valley 
    to an elevation of more than 7500 feet 
    above sea level. The butte is located just 
    north of US 30N and the Union Pacific Railroad, 
    which traverse the valley. ''',

             '''At the base of Fossil Butte are the bright 
             red, purple, yellow and gray beds of the Wasatch 
             Formation. Eroded portions of these horizontal 
             beds slope gradually upward from the valley floor 
             and steepen abruptly. Overlying them and extending 
             to the top of the butte are the much steeper 
             buff-to-white beds of the Green River Formation, 
             which are about 300 feet thick.''',

             '''The monument contains 8198 acres and protects 
             a portion of the largest deposit of freshwater fish 
             fossils in the world. The richest fossil fish deposits 
             are found in multiple limestone layers, which lie some 
             100 feet below the top of the butte. The fossils 
             represent several varieties of perch, as well as 
             other freshwater genera and herring similar to those 
             in modern oceans. Other fish such as paddlefish, 
             garpike and stingray are also present.'''
             )
    txt_selcetion = input('Enter a number 1-3 to select:')

    if txt_selcetion.isnumeric() and int(txt_selcetion) in range(1, 4):
        txt_selcetion = int(txt_selcetion) - 1

    else:
        print('Wrong choice, choose a number in range 1-3.')
        exit()

num_str: int = 0
title = 0
upper = 0
lower = 0
num_nu = 0
sum_num = 0
length_w = []


for word in TEXTS[txt_selcetion].split():
    TEXTS = word.strip(",.")
    num_str += 1
    length_w.append(len(TEXTS))

    if word[0].istitle():
        title += 1
    elif word.isupper():
        upper += 1
    if word.islower():
        lower += 1
    if word.isnumeric():
        num_nu += 1
        sum_num += int(TEXTS)

print('=' * 40)
print(f"There are {num_str} words in the selceted texts.")
print(f"There are {title} titlecase words..")
print(f"There are {upper} uppercase words.")
print(f"There are {lower} lowercase words.")
print(f"There are {num_nu} numeric strings.")
print(f"The sum of all the numbers {sum_num}.")

print('=' * 40)
print("LEN | OCCURANCES | NUMBER")
print(('=' * 40))

for lenght in sorted(set(length_w)):
    num_lenght = length_w.count(lenght)
    print(lenght, "*" * num_lenght, num_lenght)
