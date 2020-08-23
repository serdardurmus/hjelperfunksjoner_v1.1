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

en_liste = [1,2,3]
result = temp = []
for i in en_liste:
    for j in en_liste:
        for k in en_liste:
            if i != j and j != k and i != k:temp.append([i,j,k])
            if( temp not in result) and (temp != []): result+= temp
            else: pass
            temp = []
print(result)
