__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1360/B
B. Honest Coach
'''


t = int(input())

for _ in range(t):
      MIN = []
      n = int(input())
      athletes = sorted(list(map(int, input().split())))
      for i in range(n - 1):
            MIN.append(athletes[i+1] - athletes[i])
      print(min(MIN))
      
