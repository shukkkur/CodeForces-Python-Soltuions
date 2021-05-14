__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/25/A
A. IQ test
'''


n = int(input())
nums = list(map(int, input().split()))
loc = {}

for idx, val in enumerate(nums):
      if val % 2 == 0:
            loc[idx] = True 
      else:
            loc[idx] = False
            
if sum(loc.values()) > 1:
      for k, v in loc.items():
            if v == False:
                  print(k+1)
else:
      for k, v in loc.items():
            if v == True:
                  print(k+1)
            




