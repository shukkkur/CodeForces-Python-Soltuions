__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1399/A
A. Remove Smallest
'''

for _ in range(int(input())):
      n = int(input())
      a = set(map(int, input().split()))
      print('YES' if max(a)-min(a) < len(a) else 'NO')
