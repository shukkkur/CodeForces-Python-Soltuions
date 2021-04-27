__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/69/A
'''


n = int(input())
x, y, z = 0, 0, 0

for i in range(n):
      arr = list(map(int, input().split()))
      x += arr[0]
      y += arr[1]
      z += arr[2]

if x == y == z == 0:
      print('YES')
else:
      print("NO")
