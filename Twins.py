__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/160/A
'''


n = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

twin1 = 0
count = 0

while twin1 <= sum(arr):
      twin1 += arr.pop(0)
      count += 1
      

print(count)
