__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1551/A
A. Polycarp and Coins
'''


t = int(input())

for _ in range(t):
      n = int(input())
      c2 = round(n / 3)
      c1 = n - 2*c2
      print(c1, c2)
