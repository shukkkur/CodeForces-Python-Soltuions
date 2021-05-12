__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/443/A
A. Anton and Letters
'''


s = set(list(map(str.strip, input().strip('{}').split(','))))
temp = s.copy()
for i in s:
      elem = temp.pop()
      if elem != '':
            temp.add(elem)

print(len(temp))
