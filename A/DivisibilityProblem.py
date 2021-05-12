__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1328/A
A. Divisibility Problem
'''


n = int(input())

for _ in range(n):
      a, b = map(int, input().split())
      c = (a + b) - (a % b) # closest integer that is greater than a 
      print(c - a) if a % b != 0 else print(0)
