# Task : Write a program that takes a number from the user and prints 
# the result to check if it is a prime number.

antallet = input("Vennligst skriv et antall: ")
while True:
    if antallet.isnumeric() == True: break
    else: antallet = input("Vennligst skriv bare et positiv antall: ")

antallet = int(antallet)
if antallet == 0 or antallet == 1: print(f"{antallet} is not a prime number")
elif antallet == 2: print(f"{antallet} is a prime number")
else:
    prime = True
    for i in range(2,antallet):
        if antallet%i == 0: prime = False
    if prime: print(f"{antallet} is a prime number")
    else: print(f"{antallet} is not a prime number")