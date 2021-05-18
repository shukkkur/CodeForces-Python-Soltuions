__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1335/A
A. Candies and Two Sisters
'''


t = int(input())

for _ in range(t):
      count = 0
      n = int(input())
      if n == 1 or n == 2:
            print(count)
            continue 
      elif n % 2 == 1:
            count = n // 2
      else:
            count = (n // 2) - 1
      print(count)
