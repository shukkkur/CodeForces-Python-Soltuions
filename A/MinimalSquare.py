__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1360/A
A. Minimal Square
'''


t = int(input())

for _ in range(t):
      vals = list(map(int, input().split()))
      l = max(vals)
      w = min(vals)

      if w * 2 < l:
            print(l**2)
      else:
            print(4*(w**2))



