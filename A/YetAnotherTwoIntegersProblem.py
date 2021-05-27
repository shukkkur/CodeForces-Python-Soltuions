__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1409/A
A. Yet Another Two Integers Problem
'''


n = int(input())

for _ in range(n):
      a, b = map(int, input().split())
      diff = abs(a - b)
      if a == b:
            print(0)
      elif diff % 10 == 0:
            print(diff // 10)
      else:
            print(int((diff / 10) + 1))
