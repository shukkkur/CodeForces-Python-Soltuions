__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/451/A
A. Game With Sticks
'''


h, v = sorted(list(map(int, input().split())))
sticks = h + v
points = h * v
winner = 0

while points != 0:
      if h != 0:
            h -= 1
            points = h * v
            winner += 1
      elif v != 0:
            v -= 1
            points = h * v
            winner += 1

print('Akshat') if (winner % 2 == 1) else print('Malvika') 
