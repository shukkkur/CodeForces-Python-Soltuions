__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/520/A
A. Pangram
'''
n = input()
alphabet = sorted(set('abcdefghijklmnopqrstuvwxyz'))

s = sorted(set(input().lower()))

print('YES') if alphabet == s else print('NO')






