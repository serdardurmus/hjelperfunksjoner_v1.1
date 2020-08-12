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