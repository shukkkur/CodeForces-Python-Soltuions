__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/427/A
A. Police Recruits
'''


n = int(input())
events = list(map(int, input().split()))

officers = 0
untreated = 0

for event in events:
      if event == -1:
            if officers <= 0:
                  untreated += 1
            else:
                  officers -= 1
      else:
            officers += event

print(untreated)
