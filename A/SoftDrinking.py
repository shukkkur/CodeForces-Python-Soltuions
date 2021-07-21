__author__ = 'shukkkur'


'''
A. Soft Drinking
https://codeforces.com/problemset/problem/151/A
'''


n, k, l, c, d, p, nl, np = map(int, input().split())

ml = (k * l)//nl
slices = c * d
salt = p // np

print(min(ml, slices, salt)//n)
