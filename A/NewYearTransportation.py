__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/500/A
A. New Year Transportation
'''


n, t = map(int, input().split())
portals = list(map(int, input().split()))
position = 0

while position < t-1:
      position += portals[position]
      
print('YNEOS'[position>=t::2])



