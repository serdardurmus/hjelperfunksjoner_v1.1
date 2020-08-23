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

xx = [1, 2, 3, 4]
result = [[]]
for j in xx:
    my_perms = []
    for p in result:
        for i in range(len(p)+1):
            my_perms.append(p[:i] + [j] + p[i:])
            result = my_perms
print(result)