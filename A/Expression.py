__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/479/A
'''

a = int(input())
b = int(input())
c = int(input())

c1 = a + b * c
c2 = a * (b + c)
c3 = a * b * c
c4 = (a + b) * c
c5 = a + b + c

print(max(c1,c2,c3,c4, c5))
