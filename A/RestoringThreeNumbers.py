__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1154/A
A. Restoring Three Numbers
'''


vals = list(map(int, input().split()))
t = vals.pop(vals.index(max(vals)))
x,y,z = vals

c = t - x
a = y - c
b = z - c

print(a, b, c)
