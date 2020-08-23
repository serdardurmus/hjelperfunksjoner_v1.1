"""
Task:

Count the number of each letter in a sentence.
The department you work for undertook a project construction that makes word / text analysis. You are asked to calculate the number of letters or any chars in the sentences entered under this project.
Write a Python program that;
takes a sentence from the user,
counts the number of each letter of the sentence,
collects the letters/chars as a key and the counted numbers as a value in a dictionary.
"""

en_setning = input("Vennligst skriv en setning: ")
teller = {}

def sjekke(telle, bokstav):
    count = 0
    if bokstav not in telle: 
        telle[bokstav] = 1
    else: telle[bokstav] = (telle[bokstav] + 1)
    return telle[bokstav]

for i in en_setning:
    result = sjekke(teller, i)

print(teller)