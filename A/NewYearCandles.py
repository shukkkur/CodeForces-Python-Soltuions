__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/379/A
A. New Year Candles
'''


a, b = map(int, input().split())
candles = 0
counter = 0

while a > 0:
      candles += 1
      counter += 1
      if counter == b:
            a += 1
            counter = 0
      a -= 1 

print(candles)
