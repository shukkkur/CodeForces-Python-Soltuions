__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/318/A
'''


from math import  floor
n, k = map(int, input().split())

odds = range(1, n+1, 2)
evens = range(2, n+1, 2)

try:
      print(odds[k-1])
except IndexError:
      try:
            idx = k - len(odds)
            print(evens[idx-1])
      except OverflowError:
            try:
                  idx = k - floor(n/2)
                  print(evens[idx-1])
            except IndexError:
                  print(evens[idx-2])
