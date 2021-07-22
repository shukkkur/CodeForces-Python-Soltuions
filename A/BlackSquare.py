__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/431/A
A. Black Square
'''


weights = list(map(int, input().split()))
s = input()

cal = 0

for box in s:
      cal += weights[int(box)-1]

print(cal)


