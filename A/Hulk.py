__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/705/A
'''

n = int(input())
edgeOdd= 'I hate it'
edgeEven = 'I love it'
middleOdd = 'I hate that'
middleEven = 'I love that'

for i in range(1, n+1):
      if n == 1:
            print(edgeOdd, end=' ')
      elif i == range(n+1)[-1]:
            print(edgeEven, end=' ') if range(n+1)[-1] % 2 == 0 else print(edgeOdd, end=' ')
      else:
            print(middleEven, end=' ') if i % 2 == 0 else print(middleOdd, end=' ')
      

