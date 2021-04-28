__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/136/A
'''


n = int(input())
pi = list(map(int, input().split()))
count = 1
order = []

while len(order) != len(pi):
      for idx, val in enumerate(pi, start=1):
            if val == count:
                  order.append(str((idx)))
                  count += 1
                  
print(' '.join(order))
      


                
