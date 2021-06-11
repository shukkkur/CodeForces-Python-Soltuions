__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1367/B
B. Even Array
'''

t = int(input())

for _ in range(t):
      n = int(input())
      arr = list(map(int, input().split()))

      # modes of indexes
      if n % 2 == 0:
            i = [0, 1] * (n//2) #
      else:
            i = ([0, 1] * (n//2)) + [0]

       # modes of values    
      mod = [val%2 for val in arr]

      if sorted(mod) == sorted(i):
            moves = 0
            for j in range(n):
                  if i[j] != mod[j]:
                        moves += 1
            print(moves//2)
      else:
            print(-1)
