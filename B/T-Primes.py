__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/230/B
B. T-primes

Helpful Resources:
https://www.quora.com/How-do-I-solve-Codeforces-T-prime-problem
'''


n = 1000000
input()
nums = list(map(int, input().split()))
empty = [1] * n 
s = set()

for i in range(2, n):
      if empty[i]:
            s.add(i * i)
            for j in range(i * i, n, i):
                  empty[j] = 0
 
for num in nums:
      print(["NO","YES"][num in s])
