__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1472/B
B. Fair Division
'''

t = int(input())

for _ in range(t):
      n = int(input())
      weights = list(map(int, input().split()))
      if sum(weights) % 2 == 0:
            target = sum(weights) // 2
            c = 0
            temp = weights.copy()
            for weight in sorted(weights, reverse=True):
                  if c + weight <= target:
                        c += weight
                        temp.pop(temp.index(weight))
      
            if sum(temp) == target:
                  print('YES')
            else:
                  print('NO')
      else:
            print('NO')
