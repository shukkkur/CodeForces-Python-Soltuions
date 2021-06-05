__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1343/A
A. Candies
'''


t = int(input())

for i in range(t):
      n = int(input())

      for k in range(2, 10**9):
            x = n % (2**k-1)
            if x == 0:
                  print(int(n / (2**k-1)))
                  break
