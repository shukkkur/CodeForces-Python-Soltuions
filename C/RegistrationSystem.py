__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/4/C
C. Registration system
'''


n =  int(input())
database = {}

for i in range(n):
      name = input()
      
      if name not in database:
            database[name] = 1
            print('OK')
      else:
            print(name + str(database[name]))
            database[name] += 1

