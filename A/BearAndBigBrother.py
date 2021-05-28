__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/791/A
A. Bear and Big Brother
'''


Limak, Bob = map(int, input().split())
years = 0

if Limak == Bob:
      years += 1
      print(years)
else:
      while Limak <= Bob:
            Limak *= 3
            Bob *= 2
            years += 1
      print(years)
