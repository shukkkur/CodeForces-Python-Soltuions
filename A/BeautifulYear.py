__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/271/A
'''


def uniqueYear(st: str):
      st = sorted(st)
      for i in range(len(st)-1):
            if st[i] == st[i+1]:
                  return False
      return True

year = str(int(input())+1)

while not uniqueYear(year):
      year = str(int(year)+1)
      
print(year)










