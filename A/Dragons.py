__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/230/A
A. Dragons
'''

s, n = map(int, input().split())
capable = True
dragons = []

for _ in range(n):
      dragons.append(tuple(map(int, input().split())))

dragons.sort()

for dragon in dragons:
      if s <= dragon[0]:
            capable = False
      else:
            s += dragon[1]

print('YES') if capable else print('NO')





      
