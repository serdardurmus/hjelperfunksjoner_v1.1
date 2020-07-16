# Fibonacci 
antall = int(input("Skriv det siste nummeret av Fibonacci-listen du vil se: "))
listeen= []
a = 1
b = 1
while True:
    if a > antall: break
    listeen.append(a)
    if b > antall : break
    listeen.append(b)
    a = a+b
    b = a+b

print(listeen)
if listeen[-1] != antall : print("{} er ikke et fibonacci nummer".format(antall))


"""
fibonacci = [1, 1]
while fibonacci[-1] < 55:
    fibo_next = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(fibo_next)
print(fibonacci)
"""