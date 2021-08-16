__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1374/C
C. Move Brackets
'''


t = int(input())

for _ in range(t):
      n = int(input())
      s = input()
      
      while '()' in s:
            s = s.replace('()', '')
      print(s.count('(') )
##      temp = 0
##      steps = 0
##      for bracket in s:
##            if bracket == '(':
##                  temp += 1
##            else:
##                  temp -= 1
##                  if temp < 0:
##                        steps += 1
##      print(steps)


      
