__author__ = 'shukkkur'

'''
https://codeforces.com/problemset/problem/1335/B
B. Construct the String
'''
      
t = int(input())
alphabet = [*range(97, 123)]

for _ in range(t):
      
      n, a, b = map(int, input().split())
      s = ''
      unique = ''

      for char in range(b):
            unique += chr(alphabet[char])
      repeated = (unique * a)[:a]
      final = (repeated * n)[:n]
      
      print(final)
