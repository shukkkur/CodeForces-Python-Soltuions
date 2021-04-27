__author__ = 'shukkkkur'


'''
https://codeforces.com/problemset/problem/71/A
'''


testCase = int(input())

for _ in range(testCase):
      word = input()
      if len(word) > 10:
            short = word[:1] + str(len(word[1:-1])) + word[-1:]
            print(short)
      else:
            print(word)
      
