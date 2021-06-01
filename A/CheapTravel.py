__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/466/A
A. Cheap Travel
'''


n,m,a,b=map(int,input().split())
print(min(n*a,-n//m*-b,n//m*b+n%m*a))
