__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/467/A
'''


n = int(input())
count = 0

for _ in range(n):
      p, q = map(int, input().split())

      if (q - p >= 2):
            count += 1

print(count)
      


      
