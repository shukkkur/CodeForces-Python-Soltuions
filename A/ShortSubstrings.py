__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1367/A
A. Short Substrings
'''


n = int(input())

for _ in range(n):
      word = input()
      print(word[::2] + word[-1])

      
