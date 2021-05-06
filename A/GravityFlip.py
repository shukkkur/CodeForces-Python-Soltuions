__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/405/A
'''


n = int(input())
cols = sorted(list(map(int, input().split())))

print(' '.join(str(i) for i in cols))
