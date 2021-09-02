__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1426/A
A. Floor Number
'''


t = int(input())

for _ in range(t):
      n, x = map(int, input().split())
      if n <= 2:
            print(1)
      else:
            print((n-3) // x + 2)
                  
                  

      
