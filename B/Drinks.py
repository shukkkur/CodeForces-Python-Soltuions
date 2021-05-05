__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/200/B
'''


n = int(input())
props = list(map(int, input().split()))

total = sum([p/100 for p in props])

print((total/n)*100)

