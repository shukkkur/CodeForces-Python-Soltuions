__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1353/A
A. Most Unstable Array
Helpful Links:
https://www.youtube.com/watch?v=W_7C5UEvc7o
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
