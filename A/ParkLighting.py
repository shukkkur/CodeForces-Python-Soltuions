__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1358/A
A. Park Lighting
'''


t = int(input())

for _ in range(t):
      n, m  = map(int, input().split())
      nm = n * m
      if nm % 2 == 0:
            print(nm // 2)
      else:
            print((nm+1)//2)


