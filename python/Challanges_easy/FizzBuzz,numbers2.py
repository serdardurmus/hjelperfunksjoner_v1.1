# Task : Print the FizzBuzz numbers.
"""
Print numbers from 1 to 100 inclusively following these instructions:
if a number is multiple of 3, print "Fizz" instead of this number,
if a number is multiple of 5, print "Buzz" instead of this number,
for numbers that are multiples of both 3 and 5, print "FizzBuzz",
print the rest of the numbers unchanged.
Output each value on a separate line.
"""

number = 0
def FizzBuzz(number):
    if number%3 == 0 and number%5 == 0: 
        number = "FizzBuzz"
        return str(number)
    elif number%3 == 0:
        number = "Fizz"
        return str(number)
    elif number%5 == 0:
        number = "Buzz"
        return str(number)
    else: return str(number)


print("\n".join(FizzBuzz(i) for i in range(1, 100)))