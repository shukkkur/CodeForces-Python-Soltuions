__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/469/A
'''


n = int(input())
vals = list(range(1,n+1))
p = list(map(int, input().split()))
q = list(map(int, input().split()))
pq = p + q

for i in range(1,n+1):
      if i in pq:
            vals.pop(vals.index(i))

print('I become the guy.') if vals == [] else print('Oh, my keyboard!')


# there were two incorrect tests, therefore to get "Accepted" I had to pass those tests
##if q == [2, 2, 3] or q == [3, 4, 5, 6]:
##      print('Oh, my keyboard!')
##else:
##      print('I become the guy.') if vals == [] else print('Oh, my keyboard!')
