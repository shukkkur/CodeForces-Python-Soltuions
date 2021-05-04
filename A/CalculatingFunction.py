__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/486/A
'''


n = int(input())
count = 0

for i in range(1, n+1):
      if i % 2 != 0:
            count += -i
      else:
            count += i

print(count)


