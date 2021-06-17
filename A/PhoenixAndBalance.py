__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1348/A
A. Phoenix and Balance
'''


t  = int(input()) # test cases
weight = lambda x: 2**x

for _ in range(t):
      n = int(input())
      coins = [weight(i) for i in range(1, n+1)]
      a = []
      maxy = True
      for i in range(n//2):
            if maxy:
                  a.append(coins.pop(coins.index(max(coins))))
                  maxy = False
            else:
                  a.append(coins.pop(coins.index(min(coins))))
      
      print(sum(a) - sum(coins))


      
