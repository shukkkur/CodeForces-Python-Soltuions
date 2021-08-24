__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/584/A
A. Olesya and Rodion
'''


n, t = map(int, input().split())
i = int('1' +'0' * (n - 1))
j = int('1' +'0' * n)

ans = 0
for num in range(i, j):
      if num % t == 0:
            ans = num
            break

print(-1) if ans == 0 else print(ans)
