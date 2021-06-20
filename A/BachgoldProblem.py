__author__ = 'shukkkur'

'''
https://codeforces.com/contest/749/problem/A
A. Bachgold Problem
'''


n = int(input())

print(n//2)
if n % 2 == 0:
      for i in range(n//2):
            print(2, end= ' ')
else:
      for i in range(n//2-1):
            print(2, end=' ')
      print(3)
