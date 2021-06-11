__author__ = 'shukkkur'


'''
https://codeforces.com/contest/1399/problem/B
B. Gifts Fixing
'''


t = int(input())
for _ in range(t):
      n = int(input())
      candies = list(map(int, input().split()))
      oranges = list(map(int, input().split()))

      baseCandy = min(candies)
      baseOrange = min(oranges)

      steps = 0
      
      for gift in range(n):
            fixCandy = candies[gift] - baseCandy
            fixOrange =  oranges[gift] - baseOrange
            steps += max(fixCandy, fixOrange)

      print(steps)
            



      
