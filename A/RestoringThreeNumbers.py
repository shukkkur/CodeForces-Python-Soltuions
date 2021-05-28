__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1154/A
A. Restoring Three Numbers
'''


vals = list(map(int, input().split()))
t = max(vals)
vals.pop(vals.index(t))
x,y,z = vals

c = t - x
a = y - c
b = z - c

print(a, b, c)
