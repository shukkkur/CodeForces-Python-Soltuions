__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/58/A
'''


s = input()
word = 'hello'
count = 0

for i in range(len(s)):
      if s[i] == word[count]:
            count += 1
            if count == 5:
                  break

if count == 5:
      print('YES')
else:
      print('NO')
      
      




