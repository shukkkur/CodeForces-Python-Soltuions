__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1353/B
B. Two Arrays And Swaps
'''


t = int(input())

for i in range(t):
      n, k = map(int, input().split())
      a = list(map(int, input().split()))
      b = list(map(int, input().split()))

      while k > 0 and max(b) > min(a):
            temp = a[a.index(min(a))]
            a[a.index(min(a))] = max(b)
            b[b.index(max(b))] = temp
            k -= 1
      print(sum(a))
