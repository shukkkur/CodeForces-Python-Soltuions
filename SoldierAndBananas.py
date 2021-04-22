__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/546/A
'''

k, n, w = map(int, input().split())
cost = 0

for i in range(1, w+1):
      cost += i*k

if cost > n:
      print(cost - n)
else:
      print(0)
