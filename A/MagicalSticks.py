__author__ = 'shukkkur'


'''
https://codeforces.com/contest/1371/problem/A
A. Magical Sticks
'''


t = int(input())

for _ in range(t):
      n = int(input())
      if n % 2 == 0:
            print(n // 2)
      else:
            print((n+1)//2)


      
