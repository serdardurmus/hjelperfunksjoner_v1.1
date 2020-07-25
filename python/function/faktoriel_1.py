number = input("Enter a number: ")
def recur_fact(i):
    if i == 1:
       return i
    elif i < 1:
       return ("Please enter a positive number") #  In case of entering a negative number
    else:
       return i*recur_fact(i-1)
print (recur_fact(int(number))) 