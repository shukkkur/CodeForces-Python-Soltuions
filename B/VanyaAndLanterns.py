__author__ = 'shukkkur'


'''
https://codeforces.com/problemset/problem/492/B
B. Vanya and Lanterns
'''


n, l = map(int, input().split())
locs = sorted(list(map(int, input().split())))
maxDiff = 0

for i in range(len(locs)-1):
      if locs[i+1]-locs[i] > maxDiff:
            maxDiff = locs[i+1]-locs[i]            

distance = maxDiff / 2
leftEdge = min(locs)
rightEdge = l - max(locs) # l (L) is the input we took from the user

if distance < leftEdge or distance < rightEdge:
      distance = max(leftEdge, rightEdge)
      
print(distance)
