__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1433/A
A. Boring Apartments
'''
SUM = lambda x: int((x*(x+1)/2))

t = int(input())

for _ in range(t):
      x = input()
      rem =  len(x) % 4
      if rem == 0:
            print((int(x[0])-1)*10+10)
      else:
            print((int(x[0])-1)*10+SUM(rem))



      
