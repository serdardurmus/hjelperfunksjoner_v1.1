"""
This is module 1.
Welcome!
"""

def not_string(word):
    result = word
    if word[0:3] != "not": result = "not "+ word
    return result
# print(not_string("sukker"))

def factor(a):
    fac = 1
    for i in range(1,a+1):
        fac *= i
    return fac
# print(factor(5))