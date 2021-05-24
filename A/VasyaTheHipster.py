__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/581/A
A. Vasya the Hipster
'''

red, blue = map(int, input().split())
total = red + blue
a = min(red, blue)
total -= 2 * a
b = total // 2

print(a, b)



