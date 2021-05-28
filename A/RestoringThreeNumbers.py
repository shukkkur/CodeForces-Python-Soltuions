__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1154/A
A. Restoring Three Numbers

System of equations => 3 unknowns and 4 equations:
1) a + b = x        | a = x - b     |                   |
2) a + c = y        | a = y - c     | a = y - c         |
3) b + c = z        | b = z - c     | b = z - c         |
4) a + b + c = t    | a = t - b - c | x - b = t - b - c | c = t - x 

Since the input is given in a mixed order, we only care about the t = a + b + c, which is the max of all the input numbers 
'''


vals = list(map(int, input().split()))
t = vals.pop(vals.index(max(vals)))
x,y,z = vals

c = t - x
a = y - c
b = z - c

print(a, b, c)
