__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/337/A
'''


n, m = map(int, input().split())
f = sorted(list(map(int, input().split())))
val = 1000

for i in range(m - n + 1):
      temp = f[i+n-1] - f[i]
      if temp < val:
            val = temp

print(val)




