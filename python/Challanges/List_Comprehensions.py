x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))
z = int(input("Please enter a number: "))
n = int(input("Please enter a number: "))


def list_comprehensions(x,y,z,n):
    listen= []
    for i in range(0,x+1):
        for ii in range(0,y+1):
            for iii in range(0,z+1):
                if (i+ii+iii != n): listen.append([i,ii,iii])
    return listen

print(list_comprehensions(x,y,z,n))