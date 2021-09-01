__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1462/A
Favorite Sequence
'''


t = int(input())

for _ in range(t):
      n = int(input())
      old = list(map(int, input().split()))
      new = []
      i = 0
      for  i in range(n):
            if i % 2 == 0:
                  new.append(old.pop(0))
            else:
                  new.append(old.pop())
      print(' '.join(map(str, new)))









      
