# Deneme

# Write a Python code to draw whiteball and Powerball numbers for Powerball 
# lottery game. 5 Whiteball numbers are choosen from 01 to 69 and 1 Powerball 
# number is chosen 1 to 26.
"""from numpy.random import randint
for i in range(6):
    if i < 5:
        print(randint(1,69), end = ' ')
    else:
        print(' ', randint(1, 26))"""

# Let's learn some new Python concepts! You have to generate a list of the 
# first N fibonacci numbers, 0 being the first number. Then, apply the map 
# function and a lambda expression to cube each fibonacci number and print 
# the list.
"""cube = lambda x: x**3

def fibonacci(n):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, n)))
    return fib_list[:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))"""


# Additional spaces have been added to a sentence. Return the correct sentence 
# by removing them. All words should be separated by one space, and there 
# should be no spaces at the beginning or end of the sentence.
"""def correct_spacing(sentence):
    return " ".join(sentence.split())

print(correct_spacing("The film   starts       at      midnight. "))"""


# Given a list, return the most frequent (repeating) element. 
# Note : If there are the same number of repeating elements, it returns the first 
# element that repeats most from left to right in the list.

"""def most_freq(given_list):
    return max(given_list, key=given_list.count)

print(most_freq([1,2,3,3,3,3,4,4,5,5]))
print(most_freq([1,1,2,3,3]))
print(most_freq([3,1,2,1,3]))"""

# Define a function named my_fact to calculate factorial of the given number. 
# Given a non-negative integer return the factorial of the integer.
"""def my_fact(n):
    if n == 0:
        return 1
    else:
        return n* my_fact(n-1)

print(my_fact(5))"""

# String Formatting
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
"""def print_formatted(number):
    w=len(bin(number)[2:])
    for i in range(1, number+1):
        print(str(i).rjust(w) , oct(i)[2:].center(w), hex(i)[2:].center(w), bin(i)[2:].center(w))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# løsning 2
def print_formatted(number):
    results = []

    for i in range(1, n+1):
        decimal = str(i)
        octal = str(oct(i)[2:])
        hex_ = str(hex(i)[2:]).upper()
        binary = str(bin(i)[2:])

        results.append([decimal, octal, hex_, binary])

    width = len(results[-1][3])  # largest binary number

    for i in results:
        print(*(rep.rjust(width) for rep in i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)"""


# Text Alignment
"""thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
"""