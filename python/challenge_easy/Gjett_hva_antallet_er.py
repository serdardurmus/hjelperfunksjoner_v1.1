#  Prompts the user to guess the number between 1 and 100 randomly held by 
# the computer, guides if the number entered by the user is smaller or greater 
# than the number entered, and shows how many users know about the number 
# if the number is found.

import random
disk = 0
antall = random.randint(1,101)
# print(antall)
while True:
    gjett = int(input("Gjett hva antallet er? "))
    if gjett == antall:
        disk += 1
        break
    elif gjett > antall: print("skriv mindre antall")
    else: print("skriv et større antall")
    disk += 1

print(disk)