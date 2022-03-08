__author__ = 'shukkkur'


'''
B. Ordinary Numbers
https://codeforces.com/problemset/problem/1520/B
'''


t = int(input())

for i in range(t):
    n = int(input())
    l = len(str(n))
    print(9*(l-1) + n//int('1'*l))
