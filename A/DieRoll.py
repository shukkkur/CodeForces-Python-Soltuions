__author__ = 'shukkkur'


'''
A. Die Roll
https://codeforces.com/problemset/problem/9/A
'''

from fractions import Fraction

y, w = map(int, input().split())
B = 6
A = B - (max(y, w) - 1)

if A == B:
    print('1/1')
else:
    fraction = Fraction(str(A) + '/' + str(B))
    print(fraction)
