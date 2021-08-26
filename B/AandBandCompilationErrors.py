__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/519/B
B. A and B and Compilation Errors
'''


n = int(input())
errors = list(map(int, input().split()))
oneLess = list(map(int, input().split()))
twoLess = list(map(int, input().split()))

print(sum(errors)-sum(oneLess))
print(sum(oneLess)-sum(twoLess))
