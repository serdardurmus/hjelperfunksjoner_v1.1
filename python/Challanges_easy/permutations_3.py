# Given a collection of distinct integers, return all possible permutations.
"""
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
lst=list(input("enter number array for permutation"))
n=int(input("enter times of combination"))
if len(lst)>n:
    p=[[x for x in range(0)]]
    for i in range(n):
        p = [[a] + b for a in lst for b in p if (a not in b)]
    print(p)
else:
    print("Please enter a combination number lower than list length")