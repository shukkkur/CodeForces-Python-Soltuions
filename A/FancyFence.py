__author__ = 'shukkkur'


'''
https://codeforces.com/contest/270/problem/A
A. Fancy Fence
'''


t = int(input())

for _ in range(t):
      a = int(input())
      print("YES") if 360%(180-a)==0 else print("NO")

