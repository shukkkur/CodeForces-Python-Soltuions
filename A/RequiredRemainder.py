__author__ = 'shukkkur'


'''
A. Required Remainder
https://codeforces.com/problemset/problem/1374/A
'''


t = int(input())

for _ in range(t):
      x, y, n = map(int, input().split())
      q = n // x
      mode = n % x
      ans = x * q + y 
      if ans <= n:
            print(ans)
      else:
            print(x * (q - 1) + y)
