__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/677/A
'''


n, h = map(int, input().split())
heights = list(map(int, input().split()))
width = 0

for height in heights:
      if height <= h:
            width += 1
      else:
            width += 2

print(width)



