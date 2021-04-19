__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/282/A
'''

n = int(input())
outcome = 0

for _ in range(n):
      value = input()

      if value.strip('+') == 'X':
            outcome += 1
      else:
            outcome -= 1

print(outcome)
