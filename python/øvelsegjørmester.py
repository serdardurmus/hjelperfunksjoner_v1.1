# OOP Tutorial_2
"""class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1)
print(emp_2)


# print(emp_1.mail)
print(emp_2.fullname())
print(Employee.fullname(emp_1))"""

# OOP Tutorial_1
"""class PlayStation(object):
    #model = "PS4"
    #price = 99
    def __init__(self, model, price):
        "initialize properties"
        #pass
        self.model = model
        self.__price = price
    def set_price(self, price):
        self.__price = price
    def get_price(self):
        return self.__price
    def save_more(self):
            if self.amount >= self.__price:
                self.buying_message = "Yippee! You can buy your " + self.model
            elif self.amount > self.__price/2:
                self.buying_message = "You saved more than half, keep saving!"
            elif self.amount <= self.__price/2:
                self.buying_message = "You must save more, keep saving!"
model = "PS4"
price = 99
playstation1 = PlayStation(model, price)
playstation1.set_price(price)
#playstation1.amount=25
#playstation1.amount=50
playstation1.amount=100
playstation1.save_more()
print(playstation1.buying_message)"""




# textwrap, def
"""import textwrap

def wrap(string, max_width):
    a = textwrap.fill(string, max_width)
    return a
if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4
    result = wrap(string, max_width)
    print(result)"""

# You are given a string S.
# Your task is to find out if the string S contains: alphanumeric characters, 
# alphabetical characters, digits, lowercase and uppercase characters.
# Input Format
# A single line containing a string S.
"""s = input()
print(any(s.isalnum() for i in s))
print(any(s.isalpha() for i in s))
print(any(s.isdigit() for i in s))
print(any(s.islower() for i in s))
print(any(s.isupper() for i in s))"""



# In this challenge, the user enters a string and a substring. You have to print 
# the number of times that the substring occurs in the given string. String 
# traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
"""def count_substring(string, sub_string):
    s = 0
    for i in range(0, len(string)-1):
        a = string.find(sub_string)
        if a != -1:
            s += 1
            string = string[:a]+string[a+1:]
    return s

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)"""

# avarage, dict
"""n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
for i in student_marks:
    if i == query_name :
        a = sum(student_marks[i])/len(student_marks[i])
        print("%.2f" %a)"""


# nested list
"""a = [['Harry', 39.21], ['Berry', 38.21],['Tina', 38.21], ['Akriti', 37.21], ['Harsh', 39]]
a.sort()
b = [i for i in a if i[0] != a[0][0]]
print(b)
c = [j for j in b if j[0] == b[0][0]]
print(c)

c.sort(key=lambda x: x[1])
for i in range(len(c)):
    print(c[i][1])
"""


# nesned dict
"""scores= {'Student-1': {'Lesson-1': 57, 'Lesson-2': 46, 'Lesson-3': 58, 'Lesson-4': 81, 'Lesson-5': 85}, 'Student-2': {'Lesson-1': 85, 'Lesson-2': 56, 'Lesson-3': 51, 'Lesson-4': 69, 'Lesson-5': 67}, 'Student-3': {'Lesson-1': 68, 'Lesson-2': 76, 'Lesson-3': 87, 'Lesson-4': 57, 'Lesson-5': 56}, 'Student-4': {'Lesson-1': 78, 'Lesson-2': 93, 'Lesson-3': 88, 'Lesson-4': 38, 'Lesson-5': 54}, 'Student-5': {'Lesson-1': 50, 'Lesson-2': 46, 'Lesson-3': 78, 'Lesson-4': 81, 'Lesson-5': 75}}
max_avg = 0
avg = []
for i in scores:
    avg.append((i, sum(scores[i].values())/len(scores[i].items())))
print("Minimum average score and the looser student is ", min(avg, key = lambda x : x[1]))
print("Maximum average score and the vinner student is ", max(avg, key = lambda x : x[1]))
"""

# liste1 er inne i liste2 eller ikke
"""liste1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12],[13, 14, 15],[16, 17, 18],
[19, 20, 21],[22, 23, 24],[25, 26, 27],[28, 29, 30],[31, 32, 33]]

liste2 = [1, 27, 88, 98, 50, 9, 28, 45, 54, 66, 61, 23, 10, 33,
          22, 12, 6, 99, 63, 26, 87, 25, 77, 5, 16, 93, 99, 44,
          59, 69, 34, 10, 60, 92, 61, 44, 5, 3, 23, 99, 79, 51,
          89, 63, 53, 31, 76, 41, 49, 10, 88, 63, 55, 43, 40, 71,
          16, 49, 78, 41, 35, 97, 33, 76, 25, 81, 15, 99, 64, 20,
          33, 6, 89, 81, 44, 53, 59, 75, 27, 15, 64, 36, 72, 78,
          34, 36, 20, 41, 41, 75, 56, 30, 86, 46, 9, 42, 21, 64,
          26, 52, 77, 65, 64, 12, 38, 1, 35, 20, 73, 71, 37, 35,
          72, 38, 100, 52, 16, 49, 79]

for i in liste1:
    ortak = [z for z in i if z in liste2]
    if len(ortak) == len(i):
        print(i)
"""


# Missing Char
# To improve your defining function skills and string indexing ability.
"""
Given a non-empty string and an int n, return a new string where the character 
at index n has been removed. The value of n will be a valid index of a 
character in the original string (i.e. n will be in the range 0....len(str)-1 
inclusive).

def missing_char(word, n):
    a = ""
    for i in word:
        if word.index(i) == n: pass
        else: a += i
    return a
print(missing_char('kitchen', 1))
"""

# Exception Handling 2
"""
try:
    number1 = int(input("Please enter a nubmer: "))
    number2 = int(input("Please enter a number: "))
    division = number1 / number2
    print("The result of the division is : ", division)
except Exception as result:
    print(f"Probably it is because of '{result}' error")
"""

# Exception Handling 1
"""
a = input("Please enter a number: ")
b = input("Please enter a number: ")
try:
    print(int(a)/int(b))
except ZeroDivisionError:
    print("Bir sayının 0'a bölümü tanımsızdır")
except (TypeError, ValueError):
    print("Lütfen int değer giriniz.")
"""
# import date, datetime
"""
from datetime import date, datetime

birth = date(571, 4, 22)
vefat = date(632, 6, 8)
print(vefat-birth)
print(date.toordinal(vefat) - date.toordinal(birth))
"""

# FEIL
"""
def equal (a,b,c):
    number= [a,b,c]
    result = number.count(max(number, key=number.count))
    return result if result>1 else 0

print(equal(2,3,3))
print(equal(3,3,3))

def equall(a,b,c):
    number= [a,b,c]
    result = number.count(max(number, key=number.count))
    return lambda x,y,z: result if result>1 else 0

deneme = equall(1,1,2)
print(deneme)
"""

# func_generator !!!
"""
def func_generator(function):
    return lambda x : function(x)

myprint = func_generator(print)
print(myprint("serdar"))
mymax = func_generator(max)
print(mymax([1,2,3,4,5]))
"""

# User defined function, lambda
"""
import random
words = ["apple ", "swim ", "clock ", "me ", "kiwi ", "banana "]
number =random.randint(1,5)
def func(n):
    return lambda x: x*n

# print(*map(func(number), words), sep="\n")

"""

# User defined function, lambda
"""
def power1(n):
    return lambda x : x * n
words = ["apple ", "swim ", "clock ", "me ", "kiwi ", "banana "]
print(*map(power1(2), words), sep=" \n")
"""

# User defined function, lambda -50
"""
def myPrint_smile_sad_neutral(n):
    return lambda x: x+n

print((myPrint_smile_sad_neutral(":)"))("hello " ))
print((myPrint_smile_sad_neutral(":("))("hello " ))
print((myPrint_smile_sad_neutral(":|"))("hello " ))
"""
# User defined function, lambda -49
"""
def modfunc(n):
    return lambda x: x*n

print((modfunc(3))("Serdar " ))
print((modfunc(2))("Emre "))
print((modfunc(1))("Mert "))
"""

# User defined function, lambda
"""
def modfunc(n):
    return lambda x: x**n

result = modfunc(3)
print(result(3))
"""

# filter(), lambda
"""
sesli_harfler = ["a","e","i","o","u"]
listem = ["a","b","c","d","e","z"]

print(*(filter(lambda x: True if x in sesli_harfler else False, listem)))
"""

# filter() lambda
"""
words = ["apple", "swim", "clock", "me", "kiwi", "banana"]
print(*(filter(lambda x : len(x) < 5, words)), sep = "\n")
"""

# lambda, map
"""
words1 = ["you", "much", "hard"]
words2 = ["i", "he", "she"]
words3 = ["love", "works", "ate"]

result = map(lambda x,y,z: x+" "+y+" "+ z, words2,words3,words1)
for i in result:
    print(i)
"""

# lambda, map()
"""
nums1 = [9,6,7,4]
nums2 = [3,6,5,8]

result = map(lambda x, y: (x+y)/2, nums1, nums2)
print(list(result))
"""

# random
"""
from random import choice

city = ['Stockholm', 'Istanbul', 'Seul', 'Cape Town']
print(choice(city))  
"""

# Define your own factorial function named factor using def.
"""
def factor(a):
    fac = 1
    for i in range(1,a+1):
        fac *= i
    return fac

print(factor(5))
"""

# lambda, for loop
"""
numbers = [1,2,3,4,5,6,7,8,9]
for i in numbers:
    print(i, "=", (lambda x: "çift" if x%2 == 0 else "tek")(i), end= " ")
print()
print()
"""
# lambda, map
"""
print(*map((lambda x: str(x)+" is even" if x %2 ==0 else str(x)+" is odd"), [1,2,3,4,5,6]), sep = "\n")
"""

# def function
"""
def parrot_trouble(talking, hour):
    if talking == True and (hour <= 6 or hour >= 21): return True
    else: return False
print(parrot_trouble(True, 5))
print(parrot_trouble(False, 5))
"""

# ** kxargs
"""
def meaner(bill, rossum, guido, gates):
    avgg= (bill+ rossum+ guido +gates)/3
    return avgg
    
    

friends = {"bill": 4, "rossum":33, "guido":66, "gates":77}
print(meaner(**friends))
"""
# The Matter of Arguments
"""
even_list = []
odd_list = []
def slicer(*sayilar):
    global even_list, odd_list    
    for i in sayilar:
        if (i%2==0): even_list.append(i)
        else: odd_list.append(i)
    return even_list, odd_list

slicer(1,2,3,4,5,6,7,8,9)
print(even_list)
print(odd_list)

def slicer(*sayilar):
    even = [i for i in sayilar if i%2==0]
    odd = [j for j in sayilar if j%2!=0]
    print(even, odd, sep="\n")

slicer(1,2,3,4,5,6,7,8,9)
"""
# Correct Use of Arguments
"""
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000,"2","2","2","2","2","4")  # positional parameters have to be first.
"""

"""
print(list(i for i in "beri gel berber" if i == "e"))
"""
# list comprehension
"""
listem = []
[listem.append(i) for i in "beri gel berber" if i !="e"]
print(listem)
"""

# list comprehension
"""
letters = ["a", "b", "c", "d", "e", "i", "j", "x", "t"]

def kelime_ara(kelime):
    global letters
    return True if kelime in letters else False

print(kelime_ara("t"))
"""


# Jaså
"""
import sys

x = [1, 2, 3]
y = (1, 2, 3)

print(sys.getsizeof(x))
print(sys.getsizeof(y))
"""


# filter() function
"""
letters = ["a", "b", "c", "d", "i", "j", "x", "t", "e"]

def filterVowel(let):
    vowel = ["a", "e", "i", "o", "u"]
    if let in vowel: return True
    else: return False

print(filterVowel("e"))
print(list(filter(filterVowel, letters)))
"""

# Andre 
"""
def mutlakdeger (a):
    # Fonksiynumu tanıtan cümle yazıyorum 
    if a < 0: a = a* (-1)
    return a
print(mutlakdeger(3.4))
print(mutlakdeger(-4))
print(mutlakdeger.__doc__)
"""
# def()
"""
def islem(a,b):
    toplam = a + b
    fark = a - b
    return toplam, fark
toplam, fark = islem(3,5)
print(toplam, fark)
print(type(toplam), type(fark))
"""

# def function
"""
def calculator(a,b,c):
    if c == "+" : x = a+b
    elif c == "-" : x = a-b
    elif c == "*" : x = a*b
    elif c == "/" : x = a/b 
    else: return print("en feil")
    return x

print(calculator(3,5, "+"))
"""

# round()
"""
print(round(3.655,2))
print(round(3.665,2))
print(round(3.675,2))
print(round(3.685,2))
print(round(3.67501,2))
"""


# filter() enumerate()
"""
listeen = ["Susan", "tom", False, 0, "0", [], 5]
filter_list = filter(None, listeen)
for i in filter_list:
    print(i)

a = enumerate(listeen)
print(dict(a))
for i in a:
    print(i)
    print(type(i))
"""

# def function, import datetime, join()
"""
import datetime
def print_time(oppgave):
    print(oppgave)
    print(datetime.datetime.now())

en_liste = []
print_time("Kode begynner")
for i in range(1,11):
    en_liste.append(str(i))
print(",".join(en_liste))
print_time("Kode sluttet")
"""

# datetime.datetime()
"""
import datetime
print("Merhaba")
print(datetime.datetime.now())
for i in range(1,100): print(i)
print(datetime.datetime.now())
"""


# andre
"""
line = 10
print()
for i in range(line):
    print(' '*16+' '*19+'*'*12+' '*7+'*'*12+' '*7+'*'*(line-1-i)+'*'*(3*i+1))
for i in range(line*2-7):
    print(' '*(line+5-i)+'*'*(i+1)+'*'*12+' '*7+'*'*12+' '*7+'*'*12+' '*7+'*'*12)
for i in range(5):
    print(' '*16+'*'*19+'*'*19+'*'*12+' '*7+'*'*12)
"""

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

