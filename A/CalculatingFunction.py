__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/486/A
'''

n = int(input())

if n % 2 == 0:
      print(n // 2)
else:
      print(-1*(n+1)//2)


