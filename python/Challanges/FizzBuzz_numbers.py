# Task : Print the FizzBuzz numbers.
"""
Print numbers from 1 to 100 inclusively following these instructions:
if a number is multiple of 3, print "Fizz" instead of this number,
if a number is multiple of 5, print "Buzz" instead of this number,
for numbers that are multiples of both 3 and 5, print "FizzBuzz",
print the rest of the numbers unchanged.
Output each value on a separate line.
"""

def FizzBuzz(number):
    if number%3 == 0 and number%5 == 0: 
        number = "FizzBuzz"
        return number
    elif number%3 == 0:
        number = "Fizz"
        return number
    elif number%5 == 0:
        number = "Buzz"
        return number
    else: return number

for i in range(1, 101):
    number = FizzBuzz(i)
    print(number)

# join implements the opposite function of the split function.
# numbers should be integer.
# print("\n".join(FizzBuzz(i) for i in range(1, 100)))