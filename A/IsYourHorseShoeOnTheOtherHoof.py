__author__ = 'shukkkur'


'''
A. Is your horseshoe on the other hoof?
https://codeforces.com/problemset/problem/228/A
'''

colors = list(map(int, input().split()))
unique = set(colors)

print(len(colors) - len(unique))



