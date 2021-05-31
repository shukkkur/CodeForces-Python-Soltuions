__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1343/B
B. Balanced Array
'''

t = int(input())

for _ in range(1, t+1):
      n = int(input())
      if n/2 % 2 == 1:
            print('NO')
            continue
      evens = list(range(2, n+1, 2))
      odds = list(range(1, n-1, 2))
      odds = odds+[sum(evens)-sum(odds)]
      if sum(evens) == sum(odds):
            print('YES')
            print(*evens, *odds)
      else:
            print('NO')
