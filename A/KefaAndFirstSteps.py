__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/580/A
'''


n = int(input())
values = list(map(int, input().split()))
records = []
count = 1

for i in range(len(values)-1):
      if values[i] <= values[i+1]:
            count += 1
      else:
            records.append(count)
            count = 1

records.append(count)

print(max(records))
