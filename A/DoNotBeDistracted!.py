__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1520/A
A. Do Not Be Distracted!
'''


t = int(input())

for _ in range(t):
      n = int(input())
      days = list(input())
      new = days.copy()
      
      for i in range(n-1):
            if days[i] == days[i+1]:
                  new.remove(days[i+1])

      if len(new) != len(set(new)):
            print('NO')
      else:
            print('YES')
