__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1348/A
A. Phoenix and Balance

The general pattern is: 
One list has the has n/2 coins one of which is the coin with the maximum weight, whereas the the other coins (n/2-1 coins) are the coins with minimum weight. 
The second list has the remaining coins.
'''


t  = int(input()) # test cases
weight = lambda x: 2**x

for _ in range(t):
      n = int(input())
      coins = [weight(i) for i in range(1, n+1)]
      a = []
      maxy = True
      for i in range(n//2): # this loop creates the first list which consists of one coin with max weight and the remaining are have min weight
            if maxy:
                  a.append(coins.pop(coins.index(max(coins))))
                  maxy = False
            else:
                  a.append(coins.pop(coins.index(min(coins))))
      
      print(sum(a) - sum(coins))
