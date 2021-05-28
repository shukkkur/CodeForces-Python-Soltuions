__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/732/A
A. Buy a Shovel
'''

k, r = map(int, input().split())
shovels = 1

while (shovels * k - r) % 10 != 0 and shovels * k % 10 != 0:
      shovels += 1

print(shovels)
