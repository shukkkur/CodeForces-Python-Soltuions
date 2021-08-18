__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/327/A
A. Flipping Game
'''


n = int(input())
l = list(map(int, input().split()))

m = []
for i in range(n):
  for j in range(i, n):
          m.append(l[i:j+1].count(0) + (l[:i] + l[j+1:]).count(1))
print(max(m))




