__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1296/A
A. Array with Odd Sum
'''


t = int(input())
yes = 'YES'
no = 'NO'


for _ in range(t):
      n = int(input())
      a = list(map(int, input().split()))
      i = 0
      j = 0
      
      for num in a:
            if num % 2 == 0:
                  i = 1
            else:
                  j = 1
      if i == 1 and j == 1:
            print(yes)
      elif i == 1 and j == 0:
            print(no)
      elif i == 0 and j == 1:
            print(yes) if n % 2 != 0 else print(no)
            
      
