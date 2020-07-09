# Given a string, write a python function to check if it is palindrome or not. 
# A string is said to be palindrome if the reverse of the string is the same as 
# string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

et_ord = input("Skriv et ord: ")
if et_ord == et_ord[::-1]: print("Dette ordet er palindrome")
else: print("Dette ordet er ikke palindrome")