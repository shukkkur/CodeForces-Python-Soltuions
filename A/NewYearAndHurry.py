__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/750/A
A. New Year and Hurry
'''


n, timeInRoad = map(int, input().split())
timeAvailable = 4 * 60 - timeInRoad
count = 0


while timeAvailable > 0 and (timeAvailable - 5*(count+1)) >= 0 and count < n:
      timeAvailable -= 5 * (count + 1)
      count += 1
      
print(count)
