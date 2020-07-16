n = int(input("enter a number to check if it is a prime or not:"))

count = 0

for i in range(1, n+1) :
    if not (n % i) : count += 1
    print(i, count)

if (n == 0) or (n == 1) or (count >=3) : print(n, "is not a prime number.")
else : print(n, "is a prime number")