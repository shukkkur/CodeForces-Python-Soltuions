__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/723/A
A. The New Year: Meeting Friends
'''


x1, x2, x3 = sorted(map(int, input().split()))

d1 = abs((x3-x1)+(x2-1))
d2 = abs((x2-x1)+(x3-x2))

print(min(d1,d2))
