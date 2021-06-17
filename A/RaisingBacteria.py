__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/579/A
A. Raising Bacteria
'''


x = int(input())
c = 0

while x != 0:
      if x % 2 == 1:
            c += 1
      x //= 2
      
print(c)

