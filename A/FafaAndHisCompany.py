__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/935/A
A. Fafa and his Company
'''


n: int = int(input())
ways: int = 0

for i in range(1, n):
      if  (n - i) % i == 0:
            ways += 1
print(ways)
