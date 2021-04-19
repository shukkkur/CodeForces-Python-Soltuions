__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/158/A
'''

n, k = map(int, input().split())
scores = [int(item) for item in input().split()]

count = 0
idx = scores[k - 1]
for score in scores:
      if score >= idx and score > 0:
            count += 1
            
print(count)
