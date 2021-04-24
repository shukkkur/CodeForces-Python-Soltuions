__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/59/A
'''


s = input()
ups = sum(1 for char in s if char.isupper())
lowers = sum(1 for char in s if char.islower())

if ups == lowers:
      print(s.lower())
elif ups > lowers:
      print(s.upper())
else:
      print(s.lower())


      
