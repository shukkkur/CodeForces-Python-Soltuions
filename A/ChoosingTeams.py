__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/432/A
A. Choosing Teams
'''

n, k = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

for num in nums:
      if num <= 5 - k:
            count += 1
print(count//3)
