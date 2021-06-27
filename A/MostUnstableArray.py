__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1353/A
A. Most Unstable Array
'''


t = int(input())

for _ in range(t):
      n, m = map(int, input().split())
      if n == 1:
            print(0)
      elif n == 2:
            print(m)
      else:
            print(2*m)
            
