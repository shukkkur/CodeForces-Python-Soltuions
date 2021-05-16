__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/141/A
A. Amusing Joke
'''


guest = input()
host = input()
joke = ''.join(sorted(input()))
temp = ''.join(sorted(guest+host))

print('YES') if joke == temp else print('NO')
