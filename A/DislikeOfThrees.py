__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1560/A
A. Dislike of Threes
'''


t = int(input())

for _ in range(t):
      k = int(input())
      c = 0
      for n in range(1, 3000):
            if n % 3 != 0 and str(n)[-1] != '3': 
                  c += 1
                  if c == k:
                        print(n)
                        break
