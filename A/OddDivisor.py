__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1475/A
A. Odd Divisor
'''


t = int(input())

for _ in range(t):
      n = int(input())
      while n % 2 == 0:
            n //= 2

      if n == 1:
            print('NO')
      else:
            print('YES')
            


      
