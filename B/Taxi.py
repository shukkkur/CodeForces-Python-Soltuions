__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/158/B
'''


n = int(input())
groups = input()

count = {}
count[1] = groups.count('1')
count[2] = groups.count('2')
count[3] = groups.count('3')
count[4] = groups.count('4')

total = count[4] + count[3] + count[2] // 2
count[1] -= count[3]

if (count[2] % 2 == 1):
      total += 1;
      count[1] -= 2;

if (count[1] > 0):
      total += (count[1] + 3) // 4;

print(total)
