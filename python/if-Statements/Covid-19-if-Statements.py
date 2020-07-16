age = input("Are you a cigarette addict older than 75 years old? (Yes/No) ")
chronic = input("Do you have a severe chronic disease? (Yes/No) ")
immune = input("Is your immune system too weak? (Yes/No) ")

if (age.title()== "Yes" or chronic.title()== "Yes" or immune.title()== "Yes"):
    print("You are in risky group")
else: print("You are not in risky group")