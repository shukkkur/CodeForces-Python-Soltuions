__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/230/B
B. T-primes

Helpful Resources:
https://www.quora.com/How-do-I-solve-Codeforces-T-prime-problem 
https://stackoverflow.com/questions/46841968/fastest-way-of-testing-if-a-number-is-prime-with-python

This answer did not get accepted.
I managed to get all the way to 36th test.
'''
from math import sqrt 
 
def isPrime(n):
      if n == 2 or n == 3:
            return True
      if n & 1 == 0 or n == 1:
            return False
      d= 3
      while d * d <= n:
            if n % d == 0:
                  return False
            d= d + 2
      return True
 
 
n = int(input())
nums = list(map(int, input().split()))
 
for num in nums: # RULE: If the square root of  any number is prime -> Then is has exactly 3 factors)
      if isPrime(int(sqrt(num))) and sqrt(num).is_integer():
            print('YES')
      else:
            print('NO')
