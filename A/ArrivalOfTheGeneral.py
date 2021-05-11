__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/144/A
A. Arrival of the General
'''


n = int(input())
order = list(map(int, input().split()))
secs = 0

# Max & Min Location
idxMin = len(order) - order[::-1].index(min(order)) - 1
idxMax = order.index(max(order))


secs = idxMax + n - 1- idxMin

if idxMax > idxMin:
      secs -= 1

print(secs)
