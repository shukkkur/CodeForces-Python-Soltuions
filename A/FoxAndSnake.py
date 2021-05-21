__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/510/A
A. Fox And Snake
'''


n, m = map(int, input().split())
snake = '#'
empty = '.'
rightSide = True

for i in range(1, n+1):
      if i % 2 == 1:
            print(snake*m)
      else:
            if rightSide:
                  print(empty*(m-1) + snake)
                  rightSide = False
            else:
                  print(snake + empty*(m-1))
                  rightSide = True






