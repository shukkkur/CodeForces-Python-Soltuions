__author__ = 'shukkkur'


'''
A. Holiday Of Equality
https://codeforces.com/problemset/problem/758/A
'''


n = int(input())
citz = list(map(int, input().split()))
burles = max(citz) * n - sum(citz)

print(burles)
