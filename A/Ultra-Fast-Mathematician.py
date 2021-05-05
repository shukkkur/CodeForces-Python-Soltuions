__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/61/A
'''

n1 = input()
n2 = input()
length = len(n1)
answer = ''

for i in range(length):
      if n1[i] == n2[i]:
             answer += '0'
      else:
            answer += '1'

print(answer)




