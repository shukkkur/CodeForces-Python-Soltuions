__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/268/A
A. Games
'''


n = int(input())
colors = []
count = 0

for c in range(n):
      colors.append(list(map(int, input().split())))

for idx, team in enumerate(colors):
      for i in colors:
            if team[0] == i[1]:
                  count += 1

print(count)
