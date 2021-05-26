__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1352/A
A. Sum of Round Numbers
'''

t = int(input())

for _ in range(t):
      num = input()
      ans = []
      for idx, i in enumerate(num):
            if i != '0':
                  ans += [i + '0' * (len(num)-1-idx)]

      print(len(ans))    
      print(' '.join(ans))
