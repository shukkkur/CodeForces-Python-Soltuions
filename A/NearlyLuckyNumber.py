__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/110/A
'''


i = input()
n =   i.count('4') + i.count('7')
s = str(n)

s = s.replace('4', '')
s = s.replace('7', '')
if s == '':
      print('YES')
else:
      print('NO')
                        






