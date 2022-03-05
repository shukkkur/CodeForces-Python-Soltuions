__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1624/A
A. Plus One on the Subset
'''

m = int(input())

for _ in range(m):
    n = int(input())
    vals = list(map(int, input().split(' ')))
    print(max(vals) - min(vals))
