__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/339/B
B. Xenia and Ringroad
'''


n, m = map(int, input().split())
houses = list(map(int, input().split()))
houses.insert(0, 1)
time = 0 

t = lambda start, end: (end - start) % n  # this function counts the units of time needed from start to end

for i in range(m):
      time += t(houses[i], houses[i+1])
      
print(time)
