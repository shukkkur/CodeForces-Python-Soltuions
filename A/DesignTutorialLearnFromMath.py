__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/472/A
A. Design Tutorial: Learn from Math
'''

def checker(num: int) -> bool:
      lst = [2, 3, 5, 7]
      if num not in lst:
            if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
                  return True
            else:
                  return False
      

n = int(input())
a, b = 4, 0

while a + b != n:
      b = n - a
      if not checker(b): # if b is not composite
            a += 1
            while not checker(a):
                  a += 1
            
      
      
print(a, b)

