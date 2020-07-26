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

ord = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = []
for i in ord:
    if set(i) not in result: result.append(i)