__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/490/A
A. Team Olympiad
'''


n = int(input())
students = list(map(int, input().split()))

programming = [idx for idx, val in enumerate(students) if val == 1]
math = [idx for idx, val in enumerate(students) if val == 2]
pe = [idx for idx, val in enumerate(students) if val == 3]

if programming and math and pe:
      teams = min(len(programming), len(math), len(pe))
      print(teams)
      
      for team in range(teams):
            print(programming[team] + 1, end=' ')
            print(math[team] + 1, end=' ')
            print(pe[team] + 1)
else:
      print(0)
