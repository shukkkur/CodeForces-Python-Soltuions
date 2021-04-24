__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/122/A
'''

s = input()
n = int(s)

if n % 4 ==0 or n % 7 == 0 or n % 47 == 0:
      print('YES')
else:
      s = s.replace('4', '')
      s = s.replace('7', '')
      if s == '':
            print('YES')
      else:
            print('NO')






