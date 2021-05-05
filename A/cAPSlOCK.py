__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/131/A
'''


word = input()
ups = sum(1 for c in word if c.isupper())
lows = sum(1 for c in word if c.islower())

if word[0].islower() and lows == 1:
      print(word.capitalize())
elif len(word) == ups:
      print(word.lower())
else:
      print(word)

