# Given 2 sets of integers, M and N, 
# print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist 
# in either M or N but do not exist in both.

"""a,b = [set(input().split()) for _ in range(4)][1::2]
print(*sorted(a^b, key=int), sep='\n')"""

def sets(a,b):
    tomtlist =[]
    for i in a:
        if i not in set(b): tomtlist.append(i)
    for i in set(b):
        if i not in set(a): tomtlist.append(i)
    return tomtlist

arr1 = [2,4,5,9]
arr2 = [2,4,11, 12]
result = sets(arr1, arr2)
for i in result:
    print(i)