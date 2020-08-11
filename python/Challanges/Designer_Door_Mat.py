"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a 
new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

A single line containing the space separated values of N and M.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""

    
while True:
        
    try:
        num = (input("Tast inn to numre: ")).split()
        if int(num[0])*3 == int(num[1]):
            num1 = int(num[0])
            num2 = int(num[1])
            break
        else:
            print("Vennligst tast inn tall i henhold til reglene")
    except:
        print("Vennligst tast inn tall i henhold til reglene")

a = "-"
b = ".|."
c = "WELCOME"
s1 = int(num1/2)
s2 = 1
for i in range(num1+1):
    if int(num1/2)>1 and c != False:
        print(a*s1*3 + b*s2 + a*s1*3)
        s1 -= 1
        s2 += 2
        if s1==0: c = False
    elif s1 == 0: 
        lengt = len(a*s1*3 + b*s2 + a*s1*3)
        welcome = int(lengt/2 - 3)
        print(welcome*a + "WELCOME"+ welcome*a)
        s1 += 1
        s2 -= 2
    elif s1 <= num1/2:
        print(a*s1*3 + b*s2 + a*s1*3)
        s1 +=1
        s2 -= 2
    
