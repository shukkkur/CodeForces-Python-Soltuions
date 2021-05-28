__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/734/A
A. Anton and Danik
'''


n = int(input())
outcome = input()

anton = outcome.count('A')
danik = outcome.count('D')

if anton > danik:
      print('Anton')
elif danik > anton:
      print('Danik')
else:
      print('Friendship')
