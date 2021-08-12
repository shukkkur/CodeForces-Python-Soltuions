__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1385/A
A. Three Pairwise Maximums
'''


t = int(input())
yes = 'YES'
no = 'NO'

for _ in range(t):
      x, y, z = map(int, input().split())
      if x == y and x >= z:
            print(yes)
            a = x
            b = c = z
            print(a, b, c)
      elif x == z and x >= y:
            print(yes)
            a = x
            b = c = y
            print(a, b, c)
      elif y == z and y >= x:
            print(yes)
            a = y
            b = c = x
            print(a, b, c)
      else:
            print(no)
