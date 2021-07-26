__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1311/A
A. Add Odd or Subtract Even
'''


t = int(input())

for _ in range(t):
      a, b = map(int, input().split())

      if a == b:
            print(0)
      else:
            if a < b:
                  diff = b - a
                  if diff % 2 == 1:
                        print(1)
                  else:
                        print(2)
            else:
                  diff = b - a
                  if diff % 2 == 0:
                        print(1)
                  else:
                        print(2)
