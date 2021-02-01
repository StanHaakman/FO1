import random

# Opdracht 1 Pyramide

# pyramide_for_hoogte = int(input('Hoe hoog? '))
#
# for i in range(1, pyramide_for_hoogte * 2):
#     pyramide_steren = ''
#     for x in range(1, i + 1):
#         if x > pyramide_for_hoogte:
#             pyramide_steren = pyramide_steren.replace('*', '', 1)
#         else:
#             pyramide_steren += '*'
#
#     print(pyramide_steren)
#
# pyramide_while_hoogte = int(input('Hoe hoog? '))
#
# counter = 1
# while counter < (pyramide_while_hoogte * 2):
#     pyramide_steren = ''
#
#     inner_counter = 1
#     while inner_counter <= counter:
#
#         if inner_counter > pyramide_while_hoogte:
#             pyramide_steren = pyramide_steren.replace('*', '', 1)
#         else:
#             pyramide_steren += '*'
#
#         inner_counter += 1
#
#     print(pyramide_steren)
#     counter += 1


# Opdracht 2 Tekstcheck

# sentence_1 = str(input('Geef een zin: '))
# sentence_2 = str(input('Geef een zin: '))
#
#
# def point_of_difference(sentence_1, sentence_2):
#     length = len(sentence_1) if len(sentence_2) < len(sentence_1) else len(sentence_2)
#
#     for i in range(length):
#         if i == length - 1:
#             print('De twee zinnen zijn hetzelfde!')
#             break
#
#         if sentence_1[i] == sentence_2[i]:
#             continue
#         else:
#             print('Het eerste verschil zit op index: {}'.format(i))
#             break
#
#
# point_of_difference(sentence_1, sentence_2)

# Opdracht 3 Lijstcheck

# 1: Count functie
# 2: Grootste verschil tussen opvolgende elementen
# 3: 1'en en 0'en eisen check

# def count(lst):
#     return_dictionary = {}
#
#     for item in lst:
#         if item in return_dictionary:
#             return_dictionary[item] += 1
#         else:
#             return_dictionary[item] = 1
#
#     return dict(sorted(return_dictionary.items(), key=lambda return_dictionary: return_dictionary[0]))
#
#
# # Berijk van een lijst berekenen
# def rnge(lst):
#     minimaal = min(lst)
#     maximaal = max(lst)
#
#     bereik = maximaal - minimaal
#
#     return bereik
#
#
# def biggest_difference(lst):
#     biggest = 0
#
#     for i in range(len(lst) - 1):
#         bereik = rnge([lst[i], lst[i + 1]])
#         if bereik > biggest:
#             biggest = bereik
#
#     return biggest
#
#
# def requirements(lst):
#     repetitions = count(lst)
#
#     if repetitions.get(1) > repetitions.get(0) and repetitions.get(0) < 12:
#         print('De lijst voldoet aan de eisen')
#     elif repetitions.get(1) < repetitions.get(0):
#         print('De lijst heeft meer 0\'n dan 1\'en')
#     elif repetitions.get(0) > 12:
#         print('De lijst bevat te veel 0\'en')
#
#
# requirements([1,1,1,1,1,1,0,0,0,0,0])

# Opdracht 4 Palindroom

# def palindroom(str):
#     if str == str[::-1]:
#         print('{} is een palindroom'.format(str))
#     else:
#         print('{} is geen palindroom'.format(str))
#
#
# palindroom_test = str(input('Welk woord wil je checken? '))
#
# palindroom(palindroom_test)

# Opdracht 5 sorteren

# lst = [2, 24, 64, 2, 4, 1]
#
#
# def sort(lst):
#
#     sort_list = lst
#
#     def switch(list, i, x):
#         sort_list[i], sort_list[x] = list[x], list[i]
#
#     while True:
#         sort_action = False
#
#         for i in range(len(sort_list) - 1):
#             if sort_list[i] > sort_list[i + 1]:
#                 switch(sort_list, i, i + 1)
#                 sort_action = True
#
#         if not sort_action:
#             break
#
#     return sort_list

# Opdracht 6 Gemiddelde berekenen

# def average(lst):
#     length = len(lst)
#     som = sum(lst)
#
#     gem = som / length
#
#     return round(gem)
#
#
# def calculate_avarage(lijsten):
#     averages = []
#
#     for list in lijsten:
#         averages.append(average(list))
#
#     return averages
#
#
# print(calculate_avarage([[1, 5, 32, 20, 5, 76, 34, 234], [1, 5, 3, 2, 5, 76, 34, 234], [1, 3, 2, 5, 76, 34, 24]]))

# Opdracht 7 Random

# print('Welkom bij het raadspel. Raad en getal tussen de 0 en 100. Succes!!')
#
# goede_antwoord = random.randint(0, 100)
# guesses = 0
#
# while True:
#     user_guess = input('Uw gok: ')
#
#     try:
#         user_guess = int(user_guess)
#     except ValueError:
#         print('Dat is niet eens een cijfer!')
#         guesses += 1
#         continue
#
#     if user_guess == goede_antwoord:
#         print('Dat is het goede antwoord!!!')
#         guesses += 1
#         print('En dat in {} keer gokken!'.format(guesses))
#         break
#     elif user_guess < goede_antwoord:
#         if user_guess - goede_antwoord > 10:
#             print('Nog iets hoger!')
#         else:
#             print('Hoger')
#     elif user_guess > goede_antwoord:
#         if goede_antwoord - user_guess < 10:
#             print('Nog iets lager!')
#         else:
#             print('Lager')
#
#     guesses += 1

# Opdracht 8 Compressie

