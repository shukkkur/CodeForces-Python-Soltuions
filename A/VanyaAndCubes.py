__author__ = 'shukkkur'


'''
A. Vanya and Cubes
https://codeforces.com/problemset/problem/492/A
'''


n = int(input())
base = 1
c = 2
t = 0

while n - base >= 0:
      n -= base
      base += c
      c += 1
      t +=1

print(t)
