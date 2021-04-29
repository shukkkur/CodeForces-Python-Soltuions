__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/344/A
'''


n = int(input())
values = ''
count = 1

for _ in range(n):
      values += input()

count += values.count('00')
count += values.count('11')

print(count)
