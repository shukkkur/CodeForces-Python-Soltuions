__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1283/A
A. Minutes Before the New Year
'''


t = int(input())

for _ in range(t):
      h, m = map(int, input().split())
      minutes = h*60+m
      print(1440 - minutes)








      
