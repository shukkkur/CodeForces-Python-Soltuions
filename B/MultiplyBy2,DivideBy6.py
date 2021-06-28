__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/1374/B
B. Multiply by 2, divide by 6
'''


t = int(input())

for _ in range(t):
      n = int(input())
      count = 0
      while n > 1 and n <= 10**9:
            if n % 6 == 0:
                  n //= 6
            else:
                  n *= 2
            count += 1

      print(-1) if n >= 10**9 else print(count)
