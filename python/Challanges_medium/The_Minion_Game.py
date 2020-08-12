# The Minion Game
# Kevin and Stuart want to play the 'The Minion Game'.
# Your task is to determine the winner of the game and their score.
"""
Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

"""

string = "BANANA"
vowels = "AEIOU"
Stuart = 0
Kevin = 0
for i in range(len(string)):
    if string[i] in vowels:
        Kevin += (len(string)-i)
    else:
        Stuart += (len(string)-i)
if Kevin > Stuart:
    print("Kevin", Kevin)
elif Kevin<Stuart:
    print("Stuart", Stuart)
else: print("Draw")

# string = "BANANA"
# N, *z = len(string), 0, 0
# for i,c in enumerate(string):
#     z[int(c in "AEIOU")]+=N-i
# print(*reversed(max(zip(z,["Stuart","Kevin"]))) if z[0]!=z[1] else ["Draw"])