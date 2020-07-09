while True:
    number = input("Please enter a number: ")
    if number.isnumeric() == True: break
    else: print(" It is an invalid entry. Don't use non-numeric, float, or negative values!")
asteriks = 0
kuvvet = len(list(number))
for i in (list(number)):
    asteriks = asteriks + (int(i) ** kuvvet)
if int(number) == asteriks : print(f"{number} is an Armstrong number")
else: print(f"{number} is not an Armstrong number")

print()
print("# 0-100000 sayıları arasındaki Armstrong sayılar")
sayac = 0
number = 0
while sayac < 100000:
    asteriks = 0
    kuvvet = len(str(number))
    for i in str(number):
        asteriks = asteriks + (int(i) ** kuvvet)
    if int(number) == asteriks : print(f"{number} \tis an Armstrong number")
    sayac += 1
    number += 1