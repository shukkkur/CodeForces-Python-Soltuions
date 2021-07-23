__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1472/A
A. Cards for Friends
'''


t = int(input())

for _ in range(t):
      w, h, n = map(int, input().split())
      m = 1

      while w > 0 or h > 0:
            if w % 2 == 0:
                  w //= 2
                  m *= 2
            elif h % 2 == 0:
                  h //= 2
                  m *= 2
            else:
                  break
      print('YES') if m >= n else print('NO')




      


