__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/266/B
'''

n, t = map(int, input().split())
queue = list(input())

for _ in range(t):
      was = False
      for idx, student in enumerate(queue):
            if student == 'B' and idx != len(queue)-1 and queue[idx+1] == 'G' and was == False:
                  queue[idx], queue[idx+1] = queue[idx+1], queue[idx]
                  was = True
            else:
                  was = False
            

print(''.join(queue))



