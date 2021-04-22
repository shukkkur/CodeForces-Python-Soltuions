__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/266/A
'''


num = int(input())
stones = list(input()) # RGBBR
count = 0
for i in range(len(stones)-1):
      if stones[i] == stones[i+1]:
            count += 1

print(count)
