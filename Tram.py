__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/116/A
'''


n = int(input())
capacity= 0 
current = 0

for i in range(n):
      a, b = map(int, input().split())
      if i == 0:
            current += b
            if current > capacity:
                  capacity = current
      else:
            current -= a
            current += b
            if current > capacity:
                  capacity = current
                  
print(capacity)
      
            


