# Given a list of strings, group anagrams together.
"""
Given a list of strings, group anagrams together.
Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: :bangbang:
All inputs will be in lowercase.
The order of your output does not matter.
"""

# ord = input("Skriv noen Anagrams ord: ")
def group_anagrams(input):
    my_dict = {}
    for s in input:
        key = ''.join(sorted(s))
        if key in my_dict.keys():
            my_dict[key].append(s)
        else:
            my_dict[key] = []
            my_dict[key].append(s)
    return list(my_dict.values())
    
xx = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(xx)) 