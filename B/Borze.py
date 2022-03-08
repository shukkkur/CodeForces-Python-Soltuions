__author__ = 'shukkkur'


'''
B. Borze
https://codeforces.com/problemset/problem/32/B
'''

borze_code = input()

zero = '.'
one = '-.'
two = '--'

borze_code = borze_code.replace(two, '2')
borze_code = borze_code.replace(one, '1')
borze_code = borze_code.replace(zero, '0')

print(borze_code)
