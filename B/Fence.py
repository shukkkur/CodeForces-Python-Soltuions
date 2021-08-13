__author__ = 'shukkkur'


'''
B. Fence
https://codeforces.com/problemset/problem/363/B
'''


n,k = map(int,input().split())

list=[int(x) for x in input().split()]
tol=sum(list[:k])
res=[]
res.append(tol)
for i in range(n-k):
  tol+=(-list[i]+list[i+k])
  res.append(tol)
print(res.index(min(res))+1)
