while True:
    number = int(input("Please enter a number: "))
    if ((number >= 1) and (number <= 9)): break
    print("Enter numbers between 1 and 9, except 0")

# 4 farklı çözüm
print(number + 11*number + 111*number)
print(number * 123)
print(number + int(str(number)+str(number))+ int(str(number)+str(number)+str(number)))
print(number + int(str(number)*2)+ int(str(number)*3))