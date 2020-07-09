line = 10
print()
for i in range(line):
    print(' '*16+' '*19+'*'*12+' '*7+'*'*12+' '*7+'*'*(line-1-i)+'*'*(3*i+1))
for i in range(line*2-7):
    print(' '*(line+5-i)+'*'*(i+1)+'*'*12+' '*7+'*'*12+' '*7+'*'*12+' '*7+'*'*12)
for i in range(5):
    print(' '*16+'*'*19+'*'*19+'*'*12+' '*7+'*'*12)

#  nested for loop
"""
names = ["susan ", "tom ","adward "]
mood = ["happy", "sad"]
for i in names:
    for ii in mood:
        print(f"{i} is {ii}" )
"""

# for loop
"""
for i in (range(1,10)):
    print(" ",(" "*(9-i)), (str(i)*i), (str(i)*i))
for i in (range(9,0,-1)):
    print(" ",(" "*(9-i)), (str(i)*i), (str(i)*i))
"""

# counter, for loop, range, plus
"""
plus = 0
for i in range(1,75):
    plus = plus + i
print(plus)
"""

# for loop
"""
for i in range(1,10):
    print(str(i)*i)
for i in range(9,0,-1):
    print(str(i)*i)
"""

# Evens og Odds
"""
listeen = [11, 2, 24, 61, 48, 33 , 3]
evens = 0
odds = 0
for i in listeen:
    if not i%2: evens += 1
    else: odds += 1
print("The number of even numbers: {}".format(evens))
print("The number of odd numbers: {}".format(odds))
"""

# Evens og Odds 2
"""
listeen = [11, 2, 24, 61, 48, 33 , 3]
evens = 0
odds = 0
for i in listeen:
    if i%2 == 0: evens += 1
    else: odds += 1
print("The number of even numbers: {}".format(evens))
print("The number of odd numbers: {}".format(odds))
"""

# range, list, append
"""
evens = []
odds = []
for i in range(0,10):
    if i%2 == 0: evens.append(i)
    else: odds.append(i)
print(evens)
print(odds)
"""

# zip, for loop
# zip til dict
"""
text= ["a","b","c","d","e"]
number = [1,2,3,4,5]
sist = []
for i,j in zip(text, number):
    print(i,":",j)

print(list(zip(text, number)))
print(dict(zip(text, number)))
print(tuple(zip(text, number)))
print(set(zip(text, number)))
"""

# ganger 
"""
# number = int(input("0-9 arası bir rakam gir: "))
# for i in range(11):
#     print(number, "x", i, "=", (number*i))
#     print(f"{number} x {i} = {number*i}")
#     print("{} x {} =".format(number,i), number*i)
"""

# asterix, range
"""
print(tuple(range(5)))
print(*range(5))
print(*range(5), sep=", ")
print(range(5))
print(*range(5,25,2))
print(*range(10,0,-2))
"""