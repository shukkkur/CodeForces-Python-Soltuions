__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/703/A
A. Mishka and Game
'''


n = int(input())
m = 0
c = 0
for i in range(n):   
    a,b = [int(i) for i in input().split()]
    if a > b:
        m += 1
    if b > a:
        c += 1
if m > c:
    print('Mishka')
if c > m:
    print('Chris')
if c == m:
    print('Friendship is magic!^^')
