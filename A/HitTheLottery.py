__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/996/A
A. Hit the Lottery
'''

n = int(input())
bills = [100, 20, 10, 5, 1]
c = 0

while n > 0:
      if (n >= bills[0]) and (n % bills[0] != n):
            c =c + (n // bills[0])
            n %= bills[0]
      else:
            bills.pop(0)

print(c)


