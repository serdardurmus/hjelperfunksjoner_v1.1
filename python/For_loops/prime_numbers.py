# Task : Print the prime numbers which are between 1 to entered limit number (n).
"""
- You can use a nested for loop.
- Collect all these numbers into a list

The desired output for n=100 :
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
61, 67, 71, 73, 79, 83, 89, 97]
"""

tallet = input("Vennligst skriv et antall: ")

while True:
    if tallet.isnumeric() == False: tallet = input("Vennligst skriv et positiv, integer tall: ")
    else: 
        tallet = int(tallet)
        tall_list = []
        break
for i in range(2, tallet+1):
    count = 0
    for j in range(1, i+1) :
        if not (i % j) : count += 1
    if (tallet == 0) or (tallet == 1) or (count >=3) : pass
    else: tall_list.append(j)

print(tall_list)