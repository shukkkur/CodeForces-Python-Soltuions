__author__ = 'shukkkur'


'''
A. Special Permutation
https://codeforces.com/problemset/problem/1454/A
'''


t = int(input())

for _ in range(t):
      p = [*range(int(input()), 0, -1)]
      if len(p) > 2:
            p[len(p)//2], p[len(p)//2 + 1] = p[len(p)//2 + 1], p[len(p)//2]
            print(*p)
      else:
            print(*p)
