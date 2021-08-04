__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1294/A
A. Collecting Coins
'''

t = int(input())

for _ in range(t):
      a, b, c, n = map(int, input().split())
      total = a + b + c + n
      
      if (a + b + c + n) % 3 == 0 and max(a,b,c) <= total // 3:
            print('YES')
      else:
            print('NO')
